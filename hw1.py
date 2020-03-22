from typing import List
import datetime

import pandas as pd

CONFIRMED_CASES_URL = f"https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data" \
                      f"/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv "

confirmed_cases = pd.read_csv(CONFIRMED_CASES_URL, error_bad_lines=False)



def poland_cases_by_date(day, month, year: int = 2020) -> int:
  d = datetime.date(year,month,day)
  d1 = d.strftime('%m/%d/%y').lstrip("0").replace(" 0", " ").replace("/0","/")
  polska = confirmed_cases.loc[confirmed_cases["Country/Region"]=="Poland"]
  result = polska[d1].values[0]
  return result

def top5_countries_by_date(day: int, month: int, year: int = 2020) -> List[str]:
  d = datetime.date(year, month, day)
  d1 = d.strftime('%m/%d/%y').lstrip("0").replace(" 0", " ").replace("/0","/")
  countries = confirmed_cases[["Country/Region", d1]].groupby(["Country/Region"]).sum().sort_values(by=d1, ascending=False).head(5)
  return list(countries.index)

def no_new_cases_count(day: int, month: int, year: int = 2020) -> int:
  d = datetime.date(year, month, day)
  d2 = d.strftime('%m/%d/%y').lstrip("0").replace(" 0", " ").replace("/0","/")
  wczoraj = d - datetime.timedelta(days=1)
  wczoraj_str = wczoraj.strftime('%m/%d/%y').lstrip("0").replace(" 0"," ").replace("/0","/")
  return len(confirmed_cases.loc[confirmed_cases[d2] - confirmed_cases[wczoraj_str]!=0].index)
