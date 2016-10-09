# beagle
Interactive Dataset Exploration

Imagine you have a new dataset, that can be loaded into a pandas dataframe, and you want to get a rough idea of what you're looking at. You can spend time coding all sorts of plots, or load in into a visualization package and drag-and-drop endlessly, or you can use a data exploration tool, like Beagle. Beagle is inspired by [Voyager](https://github.com/vega/voyager), and is in pre-alpha stage.

TODO:
- Make generation of plots actually interactive, instead of pre-generate (requires webserver. Flask?)
- Make generation of HTML prettier (needs templating engine. Jinja?)
- Add more visualisations, allowing more dimentions to be joined.
- Create possibility to have plots that are different in dimention (double wide for example, for a side-by-side plot)
