import pandas as pd
from streamlit_vizzu import VizzuChart, Data, Config, Style
from gui import select_file


def create_charts(file):
    d_types = {
        "Address": str,
        "City": str,
        "State": str,
        "Zip": str,
        "Property Type": str,
        "Status": str,
        "Extended Status": str,
        "Listing Date": str,
        "Listing Price": float,
        "Sold Date": str,
        "Sold Price": float,
        "Beds": float,
        "Baths": float,
        "Square Ft": float,
        "Lot Size": float,
        "Year Built": float,
        "Days on Site": float,
        "Next Open House Start Time": str,
        "Next Open House End Time": str,
        "URL": str,
        "MLS#": str,
        "Favorite": str,
        "Latitude": float,
        "Longitude ": float,
    }

    with open(file, "r") as file:
        df = pd.read_csv(file, dtype=d_types)
        data = Data()
        data.add_df(df)

        chart = VizzuChart()
        chart.feature("tooltip", True)
        chart.animate(data)

        chart.animate(
            Data.filter(None),
            Config(
                {
                    "coordSystem": "cartesian",
                    "geometry": "rectangle",
                    "x": None,
                    "y": {"set": None, "range": {"min": "auto", "max": "auto"}},
                    "color": "Zip",
                    "lightness": None,
                    "size": ["Zip", "mean(Listing Price)"],
                    "noop": None,
                    "split": False,
                    "align": "none",
                    "orientation": "horizontal",
                    "label": "mean(Listing Price)",
                    "sort": "none",
                }
            ),
            Style(
                {
                    "plot": {
                        "yAxis": {"label": {"numberScale": "shortScaleSymbolUS"}},
                        "xAxis": {"label": {"numberScale": "shortScaleSymbolUS"}},
                        "marker": {
                            "label": {
                                "numberFormat": "prefixed",
                                "maxFractionDigits": "1",
                                "numberScale": "shortScaleSymbolUS",
                            },
                            "rectangleSpacing": None,
                            "circleMinRadius": 0.005,
                            "borderOpacity": 1,
                            "colorPalette": "#03ae71 #f4941b #f4c204 #d49664 #f25456 #9e67ab #bca604 #846e1c #fc763c #b462ac #f492fc #bc4a94 #9c7ef4 #9c52b4 #6ca2fc #5c6ebc #7c868c #ac968c #4c7450 #ac7a4c #7cae54 #4c7450 #9c1a6c #ac3e94 #b41204",
                        },
                    }
                }
            ),
        )

        chart.show()


if __name__ == "__main__":
    create_charts(select_file())