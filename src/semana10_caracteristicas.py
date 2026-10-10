from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

from skimage import io
from skimage import color
from skimage import util

from skimage.feature import (
    local_binary_pattern
)

from skimage.measure import (
    label,
    regionprops
)

from skimage.filters import (
    threshold_otsu
)


# ==========================================================
# SEMANA 10
# HISTOGRAMAS + REGIONES + LBP
# ==========================================================

def analizar_semana10(ruta_imagen):

    # ======================================================
    # CARGAR IMAGEN
    # ======================================================

    imagen = io.imread(
        ruta_imagen
    )

    if imagen.ndim == 3:

        imagen = color.rgb2gray(
            imagen
        )

    imagen = util.img_as_float(
        imagen
    )

    # ======================================================
    # DIRECTORIO ARTIFACTS
    # ======================================================

    artifacts_dir = Path(
        "artifacts"
    )

    artifacts_dir.mkdir(
        exist_ok=True
    )

    # ======================================================
    # HISTOGRAMA
    # ======================================================

    histograma, bins = np.histogram(
        imagen.ravel(),
        bins=32,
        range=(0, 1),
        density=True
    )

    ruta_histograma = (
        artifacts_dir /
        "semana10_histograma.png"
    )

    plt.figure(
        figsize=(6, 4)
    )

    plt.hist(
        imagen.ravel(),
        bins=32,
        color="steelblue",
        edgecolor="black"
    )

    plt.title(
        "Histograma de Intensidad"
    )

    plt.xlabel(
        "Intensidad"
    )

    plt.ylabel(
        "Frecuencia"
    )

    plt.tight_layout()

    plt.savefig(
        ruta_histograma
    )

    plt.close()

    # ======================================================
    # SEGMENTACIÓN OTSU
    # ======================================================

    umbral = threshold_otsu(
        imagen
    )

    mascara = (
        imagen > umbral
    )

    # ======================================================
    # REGIONES CONECTADAS
    # ======================================================

    regiones = regionprops(
        label(
            mascara
        )
    )

    areas = [
        r.area
        for r in regiones
    ]

    if areas:

        area_media = float(
            np.mean(
                areas
            )
        )

        area_std = float(
            np.std(
                areas
            )
        )

    else:

        area_media = 0.0
        area_std = 0.0

    # ======================================================
    # LBP
    # ======================================================

    radio = 2

    puntos = 8 * radio

    lbp = local_binary_pattern(
        imagen,
        puntos,
        radio,
        method="uniform"
    )

    lbp_hist, _ = np.histogram(
        lbp.ravel(),
        bins=np.arange(
            0,
            puntos + 3
        ),
        density=True
    )

    # ======================================================
    # VECTOR DE CARACTERÍSTICAS
    # ======================================================

    vector = np.concatenate([

        np.array([

            area_media,
            area_std,
            len(regiones)

        ]),

        histograma,

        lbp_hist

    ])

    ruta_vector = (
        artifacts_dir /
        "semana10_features.npy"
    )

    np.save(
        ruta_vector,
        vector
    )

    # ======================================================
    # RESULTADO
    # ======================================================

    return {

        # ==========================
        # REGIONES
        # ==========================

        "regiones":
            len(regiones),

        "area_media":
            round(
                area_media,
                2
            ),

        "area_std":
            round(
                area_std,
                2
            ),

        # ==========================
        # LBP
        # ==========================

        "radio":
            radio,

        "puntos":
            puntos,

        # ==========================
        # VECTOR
        # ==========================

        "tam_vector":
            len(vector),

        # ==========================
        # ARCHIVOS
        # ==========================

        "histograma":
            "/artifacts/semana10_histograma.png",

        "vector":
            "artifacts/semana10_features.npy",

        "nombre_histograma":
            "semana10_histograma.png",

        "nombre_vector":
            "semana10_features.npy"

    }