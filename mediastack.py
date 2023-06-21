import http.client
import urllib.parse
import json


def get_news(params = {}):
    params = validate_params(params)

    conn = http.client.HTTPConnection('api.mediastack.com')

    params = urllib.parse.urlencode(
        params
    )

    conn.request('GET', '/v1/news?{}'.format(params))

    res = conn.getresponse()
    data = res.read()

    data = json.loads(data.decode('utf-8'))

    try:
        return data['data']
    except:
        print(f"Error accessing the API: {data['error']}")
        return


def validate_params(params={}):
    # Adds the access key, removes any parameters that shouldn't be there
    # and makes sure that only the supported values are in certain params
    valid_params = {}
    valid_params['access_key'] = 'df1c1027bc3dd38b6cddb5e53a1ec1da'
    for key, val in params.items():
        if key == 'sources':
            valid_params['sources'] = val

        elif key == 'categories':
            supported_categories = [
                "general", "business", "entertainment", "health", "science", "sports", "technology", "politics"]
            valid_cats = []
            for cat in val.split(","):
                if cat.replace("-", "") in supported_categories:
                    valid_cats.append(cat)

            valid_params['categories'] = ",".join(valid_cats)

        elif key == 'countries':
            supported_countries = ["ar", "au", "at", "br", "bg", "ca", "co", "cz", "eg", "de", "gr", "hk", "in", "id", "ie", "it", "jp", "lv", "my", "mx", "ma", "nz", "ng", "no",
                                   "pl", "pt", "ro", "rs", "sg", "sk", "za", "kr", "se", "tw", "th", "tr", "ua", "gb", "us", "ve", "ae", "ch", "si", "sa", "ph", "nl", "lt", "il", "hu", "fr", "cn", "be"]
            valid_coun = []
            for coun in val.split(","):
                if coun.replace("-", "") in supported_countries:
                    valid_coun.append(coun)

            valid_params[key] = ",".join(valid_coun)

        elif key == 'languages':
            supported_languages = ["ar", "de", "en", "es", "fr",
                                   "he", "it", "nl", "no", "pt", "ru", "se", "zh"]
            valid = []
            for item in val.split(","):
                if item.replace("-", "") in supported_languages:
                    valid.append(item)
            valid_params[key] = ",".join(valid)

        elif key == 'keywords':
            valid_params[key] = val.replace(",","")
        elif key == 'date':
            valid_params[key] = val
        elif key == 'sort':
            if val in ["published_desc","published_asc","popularity"]:
                valid_params[key] = val
        elif key == 'limit':
            valid_params[key] = val
        elif key == 'offset':
            valid_params[key] = val

        ## Add default parameters
        if "limit" not in valid_params:
            valid_params['limit'] = 100
        if "sort" not in valid_params:
            valid_params['sort'] = "published_desc"
        if "langauges" not in valid_params:
            valid_params["langauages"] = "en"
        if "countries" not in valid_params:
            valid_params["countries"] = "us"

    return valid_params
