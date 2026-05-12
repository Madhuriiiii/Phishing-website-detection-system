def extract_features(url):

    features = []

    # URL length
    features.append(len(url))

    # Number of dots
    features.append(url.count('.'))

    # Number of hyphens
    features.append(url.count('-'))

    # Presence of @ symbol
    features.append(1 if '@' in url else 0)

    # HTTPS check
    features.append(1 if 'https' in url else 0)

    # Count digits
    digit_count = sum(c.isdigit() for c in url)
    features.append(digit_count)

    return features