from pathlib import Path

import matplotlib.pyplot as plt

from skimage import color
from skimage import feature
from skimage import filters
from skimage import io
from skimage import measure
from skimage import transform
from skimage import util


# ==========================================================
# SEMANA 9
# ANALISIS DE EVIDENCIA VISUAL
# ASISTENTE INTELIGENTE DE SOPORTE TI
# ==========================================================


# ==========================================================
# RUTAS DEL PROYECTO
# ==========================================================

ROOT = Path(__file__).resolve().parent.parent

DATA = ROOT / "data"

ARTIFACTS = ROOT / "artifacts"

ARTIFACTS.mkdir(
    parents=True,
    exist_ok=True
)


RUTA_EVIDENCIA = (
    ARTIFACTS
    / "semana09_vision.png"
)


# ==========================================================
# CONFIGURACION
# ==========================================================

AREA_MINIMA = 100

ANCHO_MAXIMO = 900


# ==========================================================
# CARGAR Y PREPARAR IMAGEN
# ==========================================================

def preparar_imagen(ruta_imagen):

    ruta = Path(
        ruta_imagen
    )

    if not ruta.exists():

        raise FileNotFoundError(
            f"No se encontro la imagen: {ruta}"
        )


    # ------------------------------------------------------
    # CARGAR IMAGEN
    # ------------------------------------------------------

    imagen_original = io.imread(
        ruta
    )


    # ------------------------------------------------------
    # ELIMINAR CANAL ALPHA SI EXISTE
    # ------------------------------------------------------

    if (
        imagen_original.ndim == 3
        and imagen_original.shape[2] == 4
    ):

        imagen_original = (
            imagen_original[:, :, :3]
        )


    # ------------------------------------------------------
    # CONVERTIR A ESCALA DE GRISES
    # ------------------------------------------------------

    if imagen_original.ndim == 3:

        imagen_gris = color.rgb2gray(
            imagen_original
        )

    else:

        imagen_gris = util.img_as_float(
            imagen_original
        )


    # ------------------------------------------------------
    # REDIMENSIONAR SI ES MUY GRANDE
    # ------------------------------------------------------

    alto, ancho = imagen_gris.shape


    if ancho > ANCHO_MAXIMO:

        factor = (
            ANCHO_MAXIMO
            / ancho
        )

        nuevo_alto = int(
            alto * factor
        )

        imagen_gris = transform.resize(
            imagen_gris,
            (
                nuevo_alto,
                ANCHO_MAXIMO
            ),
            anti_aliasing=True
        )


    return (
        imagen_original,
        imagen_gris
    )


# ==========================================================
# ANALISIS DE SEMANA 9
# ==========================================================

def analizar_semana09(
    ruta_imagen,
    sigma=2.0
):

    # ======================================================
    # 1. PREPARAR IMAGEN
    # ======================================================

    (
        imagen_original,
        imagen_gris
    ) = preparar_imagen(
        ruta_imagen
    )


    # ======================================================
    # 2. CARACTERISTICAS BASICAS
    # ======================================================

    alto = int(
        imagen_gris.shape[0]
    )

    ancho = int(
        imagen_gris.shape[1]
    )

    pixeles_totales = int(
        imagen_gris.size
    )


    intensidad_minima = round(
        float(imagen_gris.min()),
        4
    )

    intensidad_maxima = round(
        float(imagen_gris.max()),
        4
    )

    intensidad_media = round(
        float(imagen_gris.mean()),
        4
    )


    # ======================================================
    # 3. CANNY
    # ======================================================

    bordes = feature.canny(
        imagen_gris,
        sigma=sigma
    )


    pixeles_borde = int(
        bordes.sum()
    )


    porcentaje_borde = round(
        (
            pixeles_borde
            / pixeles_totales
        )
        * 100,
        2
    )


    # ======================================================
    # 4. OTSU
    # ======================================================

    umbral_otsu = filters.threshold_otsu(
        imagen_gris
    )


    # ======================================================
    # 5. MASCARA BINARIA
    # ======================================================

    mascara = (
        imagen_gris
        > umbral_otsu
    )


    pixeles_objeto = int(
        mascara.sum()
    )


    pixeles_fondo = int(
        pixeles_totales
        - pixeles_objeto
    )


    porcentaje_objeto = round(
        (
            pixeles_objeto
            / pixeles_totales
        )
        * 100,
        2
    )


    porcentaje_fondo = round(
        (
            pixeles_fondo
            / pixeles_totales
        )
        * 100,
        2
    )


    # ======================================================
    # 6. REGIONES CONECTADAS
    # ======================================================

    etiquetas = measure.label(
        mascara
    )


    propiedades = measure.regionprops(
        etiquetas
    )


    regiones_detectadas = len(
        propiedades
    )


    # ======================================================
    # 7. FILTRADO DE REGIONES
    # ======================================================

    regiones_significativas = [

        region

        for region in propiedades

        if region.area >= AREA_MINIMA
    ]


    numero_regiones_significativas = len(
        regiones_significativas
    )


    # ======================================================
    # 8. AREAS
    # ======================================================

    areas = [

        int(region.area)

        for region
        in propiedades
    ]


    if areas:

        area_mayor = max(
            areas
        )

        area_menor = min(
            areas
        )

        area_promedio = round(
            sum(areas)
            / len(areas),
            2
        )

    else:

        area_mayor = 0

        area_menor = 0

        area_promedio = 0


    # ======================================================
    # 9. EVIDENCIA VISUAL
    # ======================================================

    fig, axes = plt.subplots(
        1,
        3,
        figsize=(14, 5)
    )


    # ------------------------------------------------------
    # ORIGINAL
    # ------------------------------------------------------

    if imagen_original.ndim == 3:

        axes[0].imshow(
            imagen_original
        )

    else:

        axes[0].imshow(
            imagen_original,
            cmap="gray"
        )


    axes[0].set_title(
        "Evidencia Original"
    )


    # ------------------------------------------------------
    # CANNY
    # ------------------------------------------------------

    axes[1].imshow(
        bordes,
        cmap="gray"
    )

    axes[1].set_title(
        f"Canny | sigma={sigma}"
    )


    # ------------------------------------------------------
    # OTSU
    # ------------------------------------------------------

    axes[2].imshow(
        mascara,
        cmap="gray"
    )

    axes[2].set_title(
        "Segmentacion Otsu"
    )


    for eje in axes:

        eje.axis(
            "off"
        )


    fig.suptitle(
        "Asistente Inteligente de Soporte TI - Analisis Visual",
        fontsize=14
    )


    fig.tight_layout()


    # ======================================================
    # 10. GUARDAR EVIDENCIA
    # ======================================================

    fig.savefig(
        RUTA_EVIDENCIA,
        dpi=160,
        bbox_inches="tight"
    )


    plt.close(
        fig
    )


    # ======================================================
    # 11. RESULTADO
    # ======================================================

    return {

        "imagen":
            Path(
                ruta_imagen
            ).name,

        "tipo_imagen":
            "Evidencia visual de incidente TI",

        "ancho":
            ancho,

        "alto":
            alto,

        "pixeles_totales":
            pixeles_totales,

        "intensidad_minima":
            intensidad_minima,

        "intensidad_maxima":
            intensidad_maxima,

        "intensidad_media":
            intensidad_media,

        "metodo_bordes":
            "Canny",

        "sigma":
            float(sigma),

        "pixeles_borde":
            pixeles_borde,

        "porcentaje_borde":
            porcentaje_borde,

        "metodo_segmentacion":
            "Otsu",

        "umbral_otsu":
            round(
                float(
                    umbral_otsu
                ),
                4
            ),

        "pixeles_objeto":
            pixeles_objeto,

        "pixeles_fondo":
            pixeles_fondo,

        "porcentaje_objeto":
            porcentaje_objeto,

        "porcentaje_fondo":
            porcentaje_fondo,

        "regiones":
            regiones_detectadas,

        "regiones_significativas":
            numero_regiones_significativas,

        "area_minima_filtro":
            AREA_MINIMA,

        "area_region_mayor":
            area_mayor,

        "area_region_menor":
            area_menor,

        "area_promedio":
            area_promedio,

        "evidencia":
            RUTA_EVIDENCIA.name,

        "ruta_evidencia":
            str(
                RUTA_EVIDENCIA
            )
    }


# ==========================================================
# EJECUCION DIRECTA
# ==========================================================

if __name__ == "__main__":

    print("=" * 70)

    print(
        "SEMANA 9 - ANALISIS VISUAL DE INCIDENTES TI"
    )

    print("=" * 70)


    # ======================================================
    # IMAGEN DEL PROYECTO
    # ======================================================

    ruta_prueba = (
        DATA
        / "imagen_proyecto.png"
    )


    if not ruta_prueba.exists():

        print(
            "\nNo existe:"
        )

        print(
            ruta_prueba
        )

        print(
            "\nGuarde una imagen relacionada con "
            "Soporte TI en:"
        )

        print(
            "data/imagen_proyecto.png"
        )


    else:

        resultado = analizar_semana09(
            ruta_prueba,
            sigma=2.0
        )


        # ==================================================
        # EVIDENCIA ANALIZADA
        # ==================================================

        print("\nEvidencia analizada:")
        print("-" * 70)

        print(
            f"Archivo            : "
            f"{resultado['imagen']}"
        )

        print(
            f"Tipo               : "
            f"{resultado['tipo_imagen']}"
        )


        # ==================================================
        # CARACTERISTICAS
        # ==================================================

        print("\nCaracteristicas visuales:")
        print("-" * 70)

        print(
            f"Dimensiones        : "
            f"{resultado['ancho']} x "
            f"{resultado['alto']} pixeles"
        )

        print(
            f"Pixeles totales    : "
            f"{resultado['pixeles_totales']}"
        )

        print(
            f"Intensidad minima  : "
            f"{resultado['intensidad_minima']}"
        )

        print(
            f"Intensidad maxima  : "
            f"{resultado['intensidad_maxima']}"
        )

        print(
            f"Intensidad media   : "
            f"{resultado['intensidad_media']}"
        )


        # ==================================================
        # CANNY
        # ==================================================

        print("\nDeteccion de contornos:")
        print("-" * 70)

        print(
            f"Metodo             : "
            f"{resultado['metodo_bordes']}"
        )

        print(
            f"Sigma              : "
            f"{resultado['sigma']}"
        )

        print(
            f"Pixeles borde      : "
            f"{resultado['pixeles_borde']}"
        )

        print(
            f"Cobertura bordes   : "
            f"{resultado['porcentaje_borde']}%"
        )


        # ==================================================
        # OTSU
        # ==================================================

        print("\nSegmentacion:")
        print("-" * 70)

        print(
            f"Metodo             : "
            f"{resultado['metodo_segmentacion']}"
        )

        print(
            f"Umbral Otsu        : "
            f"{resultado['umbral_otsu']}"
        )

        print(
            f"Cobertura objeto   : "
            f"{resultado['porcentaje_objeto']}%"
        )

        print(
            f"Cobertura fondo    : "
            f"{resultado['porcentaje_fondo']}%"
        )


        # ==================================================
        # REGIONES
        # ==================================================

        print("\nRegiones conectadas:")
        print("-" * 70)

        print(
            f"Regiones totales   : "
            f"{resultado['regiones']}"
        )

        print(
            f"Regiones relevantes: "
            f"{resultado['regiones_significativas']}"
        )

        print(
            f"Region mayor       : "
            f"{resultado['area_region_mayor']} pixeles"
        )

        print(
            f"Area promedio      : "
            f"{resultado['area_promedio']} pixeles"
        )


        # ==================================================
        # EVIDENCIA
        # ==================================================

        print("\nEvidencia generada:")
        print("-" * 70)

        print(
            resultado[
                "ruta_evidencia"
            ]
        )


        # ==================================================
        # INTERPRETACION
        # ==================================================

        print("\nInterpretacion para Soporte TI:")
        print("-" * 70)

        print(
            "La imagen adjunta al incidente fue procesada "
            "como evidencia visual."
        )

        print(
            "Canny permitio identificar cambios de intensidad "
            "que pueden representar limites visuales."
        )

        print(
            "Otsu permitio separar automaticamente regiones "
            "segun sus intensidades."
        )

        print(
            "Las regiones conectadas representan componentes "
            "visuales candidatos para analisis posterior."
        )

        print(
            "Esta etapa no identifica automaticamente el tipo "
            "de dispositivo o la causa de la falla."
        )

        print(
            "El resultado constituye evidencia visual que puede "
            "ser utilizada posteriormente para clasificacion, "
            "validacion o trazabilidad del incidente."
        )


        print("\n" + "=" * 70)

        print(
            "SEMANA 9 FINALIZADA"
        )

        print("=" * 70)