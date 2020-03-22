from typing import List

import pandas as pd

CONFIRMED_CASES_URL = f"https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data" \
                      f"/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv "

confirmed_cases = pd.read_csv(CONFIRMED_CASES_URL, error_bad_lines=False)


def poland_cases_by_date(day: int, month: int, year: int = 2020) -> int:
    data = datetime.date(year,month,day)
    data1 = data.strftime('%m/%d/%y').lstrip("0").replace(" 0", " ").replace("/0", "/")
    polska = confirmed_cases.loc[confirmed_cases["Country/Region"]=="Poland"]
    result = polska[data1].values[0]
      return result



def top5_countries_by_date(day: int, month: int, year: int = 2020) -> List[str]:
    data = datetime.date(year,month,day)
    data1 = data.strftime('%m/%d/%y').lstrip("0").replace(" 0", " ").replace("/0", "/")
    kraje = confirmed_cases[["Country/Region", data1]].groupby(["Country/Region"]).sum().sort_values(by=data1, ascending=False).head(5)
    return list(kraje.index)

# Function name is wrong, read the pydoc
def no_new_cases_count(day: int, month: int, year: int = 2020) -> int:
    data = datetime.date(year,month,day)
      data1 = data.strftime('%m/%d/%y').lstrip("0").replace(" 0", " ").replace("/0", "/")
        wczoraj = data - datetime.timedelta(days=1)
          wczorajstr = wczoraj.strftime('%m/%d/%y').lstrip("0").replace(" 0", " ").replace("/0", "/")
            return len(confirmed_cases.loc[confirmed_cases[data1]-confirmed_cases[wczorajstr]!=0].index)
