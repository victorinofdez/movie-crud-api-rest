import streamlit as st
import requests
from api import *
from styles import load_css
from config import BASE_URL

st.set_page_config(page_title="🎬 Movie Manager", layout="wide")
st.markdown(load_css(), unsafe_allow_html=True)

# ---------------- SESSION ----------------
if "token" not in st.session_state:
    st.session_state.token = None
if "username" not in st.session_state:
    st.session_state.username = None
if "screen" not in st.session_state:
    st.session_state.screen = "login"  # login, movies, create, view, edit, users
if "selected_movie" not in st.session_state:
    st.session_state.selected_movie = None

# ---------------- NAVIGATION ----------------
def go_to(screen, movie=None):
    st.session_state.screen = screen
    st.session_state.selected_movie = movie
    st.rerun()  # recarga la página al cambiar de pantalla

# ---------------- LOGIN ----------------
def login_view():
    st.title("🎬 Movie Manager")
    st.subheader("Iniciar sesión")
    username = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")
    if st.button("Entrar"):
        response = login(username, password)
        if response.status_code == 200:
            data = response.json()
            st.session_state.token = data["access_token"]
            st.session_state.username = username
            go_to("movies")
        else:
            st.error("Credenciales incorrectas")

# ---------------- DASHBOARD ----------------
def dashboard_sidebar():
    st.sidebar.title(f"👤 {st.session_state.username}")
    if st.sidebar.button("Ver Películas"):
        go_to("movies")
    if st.sidebar.button("Crear Película"):
        go_to("create")
    if st.sidebar.button("Ver Usuarios"):
        go_to("users")
    if st.sidebar.button("Cerrar sesión"):
        st.session_state.token = None
        st.session_state.username = None
        st.session_state.screen = "login"
        st.session_state.selected_movie = None
        st.rerun()

# ---------------- MOVIES ----------------
def movies_screen():
    st.header("🎬 Catálogo de Películas")
    response = get_movies(st.session_state.token)
    if response.status_code != 200:
        st.error("Error al cargar películas")
        return

    movies = response.json()
    search = st.text_input("🔎 Buscar por título")
    if search:
        movies = [m for m in movies if search.lower() in m["titulo"].lower()]

    cols = st.columns(3)
    for index, movie in enumerate(movies):
        with cols[index % 3]:
            st.markdown(
                f"""
                <div class="movie-card">
                    <h4>{movie['titulo']}</h4>
                    <p><b>Año:</b> {movie['anio']}</p>
                    <p><b>Director:</b> {movie['director']}</p>
                    <p>{movie['sinopsis'][:80]}...</p>
                </div>
                """,
                unsafe_allow_html=True
            )
            if st.button("👁 Ver", key=f"view_{movie['id']}"):
                go_to("view", movie)
            if st.button("✏️ Editar", key=f"edit_{movie['id']}"):
                go_to("edit", movie)
            if st.button("🗑 Eliminar", key=f"delete_{movie['id']}"):
                delete_movie(st.session_state.token, movie["id"])
                st.success("Película eliminada")
                go_to("movies")

# ---------------- VIEW MOVIE ----------------
def view_movie_screen(movie):
    st.header(f"🎬 {movie['titulo']}")
    st.write(f"**Año:** {movie['anio']}")
    st.write(f"**Director:** {movie['director']}")
    st.write(f"**Sinopsis:** {movie['sinopsis']}")
    if st.button("⬅ Volver"):
        go_to("movies")

# ---------------- EDIT MOVIE ----------------
def edit_movie_screen(movie):
    st.header(f"✏️ Editar {movie['titulo']}")
    with st.form("edit_movie_form"):
        titulo = st.text_input("Título", movie["titulo"])
        anio = st.number_input("Año", min_value=1900, max_value=2100, value=movie["anio"])
        director = st.text_input("Director", movie["director"])
        sinopsis = st.text_area("Sinopsis", movie["sinopsis"])
        submitted = st.form_submit_button("Guardar cambios")
        if submitted:
            new_data = {"titulo": titulo, "anio": anio, "director": director, "sinopsis": sinopsis}
            response = requests.put(
                f"{BASE_URL}/movies/{movie['id']}",
                json=new_data,
                headers={"Authorization": f"Bearer {st.session_state.token}"}
            )
            if response.status_code == 200:
                st.success("Película actualizada 🎉")
                go_to("movies")
            else:
                st.error("Error al actualizar película")
    if st.button("⬅ Volver"):
        go_to("movies")

# ---------------- CREATE MOVIE ----------------
def create_movie_screen():
    st.header("➕ Crear nueva Película")
    with st.form("create_movie_form"):
        movie_id = st.number_input("ID", min_value=1)
        titulo = st.text_input("Título")
        anio = st.number_input("Año", min_value=1900, max_value=2100)
        director = st.text_input("Director")
        sinopsis = st.text_area("Sinopsis")
        submitted = st.form_submit_button("Crear")
        if submitted:
            movie_data = {
                "id": int(movie_id),
                "titulo": titulo,
                "anio": int(anio),
                "director": director,
                "sinopsis": sinopsis
            }
            # ✅ Llamada corregida al backend con id y valor
            response = requests.post(
                f"{BASE_URL}/movies/",
                json=movie_data,
                headers={"Authorization": f"Bearer {st.session_state.token}"}
            )
            if response.status_code == 200 or response.status_code == 201:
                st.success("Película creada 🎬")
                go_to("movies")
            else:
                st.error("Error al crear película")
    if st.button("⬅ Volver"):
        go_to("movies")

# ---------------- USERS ----------------
def users_screen():
    st.header("👥 Usuarios")
    response = get_users(st.session_state.token)
    if response.status_code == 200:
        st.json(response.json())
    else:
        st.error("No tienes permisos para ver usuarios")
    if st.button("⬅ Volver"):
        go_to("movies")

# ---------------- MAIN ----------------
if st.session_state.token is None or st.session_state.screen == "login":
    login_view()
else:
    dashboard_sidebar()
    if st.session_state.screen == "movies":
        movies_screen()
    elif st.session_state.screen == "view" and st.session_state.selected_movie:
        view_movie_screen(st.session_state.selected_movie)
    elif st.session_state.screen == "edit" and st.session_state.selected_movie:
        edit_movie_screen(st.session_state.selected_movie)
    elif st.session_state.screen == "create":
        create_movie_screen()
    elif st.session_state.screen == "users":
        users_screen()
