## Aivo Project

### Running instruction

Make sure the dependencies are installed, 
and you have a working Python enviroment.
From the command line enter:

```bash
python app.py
```

You should get an output similar to this:
```text
* Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Depending on the port chosen, the landing page to
visit would be:  

`http://127.0.0.1:5000/`

You should see a list of countries
in ascending order by their satisfaction index.

Sample image:

![image](https://user-images.githubusercontent.com/1905839/92032785-a9be6480-ed38-11ea-9f83-afa1a51e78ae.png)
You can enter in the input form a number, 
in order to see only countries with satisfaction
indexes greater than that number.

The validation of the form, is implemented by casting 
the received input form value to a float type. 

### Future features
For building a different country list, 
it is encouraged to used the method
`get_countries_dict()`. For each country it builds a dictionary, 
with the different types of indexes. 

Below is the Austria country example:
```python
 'Austria': {'CG_SENG': {'MN': 1.3, 'TOT': 1.3, 'WMN': 1.3},
             'CG_VOTO': {'HGH': 75.0,
                         'LW': 75.0,
                         'MN': 75.0,
                         'TOT': 75.0,
                         'WMN': 74.0},
             'EQ_AIRP': {'MN': 16.0, 'TOT': 16.0, 'WMN': 16.0},
             'EQ_WATER': {'MN': 93.0, 'TOT': 93.0, 'WMN': 93.0},
             'ES_EDUA': {'MN': 88.0, 'TOT': 85.0, 'WMN': 81.0},
             'ES_EDUEX': {'MN': 16.9, 'TOT': 17.1, 'WMN': 17.4},
             'ES_STCS': {'HGH': 541.0,
                         'LW': 447.0,
                         'MN': 496.0,
                         'TOT': 492.0,
                         'WMN': 488.0},
             'HO_BASE': {'MN': 1.0, 'TOT': 1.0, 'WMN': 1.0},
             'HO_HISH': {'MN': 21.0, 'TOT': 21.0, 'WMN': 21.0},
             'HO_NUMR': {'MN': 1.6, 'TOT': 1.6, 'WMN': 1.6},
             'HS_LEB': {'MN': 78.8, 'TOT': 81.3, 'WMN': 83.7},
             'HS_SFRH': {'HGH': 81.0,
                         'LW': 59.0,
                         'MN': 72.0,
                         'TOT': 70.0,
                         'WMN': 68.0},
             'IW_HADI': {'HGH': 58911.0,
                         'LW': 14301.0,
                         'MN': 32544.0,
                         'TOT': 32544.0,
                         'WMN': 32544.0},
             'IW_HNFW': {'MN': 59574.0, 'TOT': 59574.0, 'WMN': 59574.0},
             'JE_EMPL': {'HGH': 86.0,
                         'LW': 54.0,
                         'MN': 75.0,
                         'TOT': 72.0,
                         'WMN': 68.0},
             'JE_LTUR': {'HGH': 1.03,
                         'LW': 3.54,
                         'MN': 2.2,
                         'TOT': 1.94,
                         'WMN': 1.65},
             'JE_PEARN': {'HGH': 61822.0,
                          'LW': 28935.0,
                          'MN': 52211.0,
                          'TOT': 48295.0,
                          'WMN': 40849.0},
             'PS_FSAFEN': {'MN': 84.8, 'TOT': 80.7, 'WMN': 77.0},
             'PS_REPH': {'MN': 0.5, 'TOT': 0.4, 'WMN': 0.4},
             'SC_SNTWS': {'HGH': 95.0, 'MN': 91.0, 'TOT': 92.0, 'WMN': 92.0},
             'SW_LIFS': {'HGH': 7.5,
                         'LW': 6.9,
                         'MN': 7.0,
                         'TOT': 7.0,
                         'WMN': 7.0},
             'WL_EWLH': {'MN': 10.31, 'TOT': 6.78, 'WMN': 3.03},
             'WL_TNOW': {'MN': 14.72, 'TOT': 14.55, 'WMN': 14.32}}
```




### Dependencies
Flask, Python 3