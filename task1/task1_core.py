def domain_name(url):
    base_url_elements = url.split(".")
    for item in base_url_elements:
        if "//" in item:
            url_elements = item.split("//")
        else:
            url_elements = [item]
        for element in url_elements:
            if all(
                (
                    element,
                    "www" not in element,
                    ":" not in element,
                )
            ):
                return element