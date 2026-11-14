import sqlite3
from pathlib import Path


RUTA_DB = (
    Path("artifacts")
    / "incidentes_soporte.db"
)


# ==========================================================
# CONEXION
# ==========================================================

def conectar():

    conexion = sqlite3.connect(
        RUTA_DB
    )

    conexion.execute(
        "PRAGMA foreign_keys = ON"
    )

    return conexion


# ==========================================================
# TABLAS
# ==========================================================

def crear_tablas():

    with conectar() as conexion:

        conexion.executescript(
            """
            CREATE TABLE IF NOT EXISTS dominio (

                id INTEGER PRIMARY KEY,

                nombre TEXT UNIQUE
            );

            CREATE TABLE IF NOT EXISTS aplicacion (

                id INTEGER PRIMARY KEY,

                nombre TEXT,

                dominio_id INTEGER
            );

            CREATE TABLE IF NOT EXISTS experto (

                id INTEGER PRIMARY KEY,

                nombre TEXT
            );

            CREATE TABLE IF NOT EXISTS herramienta (

                id INTEGER PRIMARY KEY,

                nombre TEXT
            );

            CREATE TABLE IF NOT EXISTS articulo (

                id INTEGER PRIMARY KEY,

                titulo TEXT,

                contenido TEXT,

                estado TEXT,

                dominio_id INTEGER,

                experto_id INTEGER
            );
            """
        )

        conexion.commit()


# ==========================================================
# DATOS
# ==========================================================

def cargar_datos():

    with conectar() as conexion:

        conexion.execute(
            """
            INSERT OR IGNORE INTO dominio
            VALUES (1,'Soporte TI')
            """
        )

        conexion.execute(
            """
            INSERT OR IGNORE INTO dominio
            VALUES (2,'Infraestructura')
            """
        )

        conexion.execute(
            """
            INSERT OR IGNORE INTO experto
            VALUES (1,'Analista Soporte')
            """
        )

        conexion.execute(
            """
            INSERT OR IGNORE INTO experto
            VALUES (2,'Administrador Infraestructura')
            """
        )

        conexion.commit()


# ==========================================================
# ARTICULOS
# ==========================================================

def crear_articulos():

    with conectar() as conexion:

        conexion.execute(
            """
            INSERT OR IGNORE INTO articulo
            VALUES
            (
                1,
                'Restablecimiento VPN',
                'Procedimiento para acceso remoto',
                'VALIDADO',
                2,
                2
            )
            """
        )

        conexion.execute(
            """
            INSERT OR IGNORE INTO articulo
            VALUES
            (
                2,
                'Cambio de contraseña',
                'Procedimiento para credenciales',
                'VALIDADO',
                1,
                1
            )
            """
        )

        conexion.commit()


# ==========================================================
# CONSULTA
# ==========================================================

def obtener_articulos():

    consulta = """

        SELECT

            titulo,
            estado

        FROM articulo

        WHERE estado =
        'VALIDADO'

    """

    with conectar() as conexion:

        return conexion.execute(
            consulta
        ).fetchall()


# ==========================================================
# ANALISIS SEMANA 15
# ==========================================================

def analizar_semana15():

    crear_tablas()

    cargar_datos()

    crear_articulos()

    articulos = obtener_articulos()

    return {

        "dominios":
            [
                "Soporte TI",
                "Infraestructura"
            ],

        "expertos":
            [
                "Analista Soporte",
                "Administrador Infraestructura"
            ],

        "articulos":
            articulos,

        "total_articulos":
            len(articulos)
    }


# ==========================================================
# PRUEBA LOCAL
# ==========================================================

if __name__ == "__main__":

    resultado = analizar_semana15()

    print(
        "\n===== SEMANA 15 =====\n"
    )

    print(resultado)