export async function fetchApi(url, kwargs) {
    // default values
    if (!kwargs.method) {
        kwargs.method = "GET";
    }

    let options = {
        method: kwargs.method,
        headers: {
            'Content-Type': 'application/json',
            "Authorization": this.current_user.authorizationHeader
        }
    }
    // add data to options if exist
    if (kwargs.data) {
        options.body = JSON.stringify(kwargs.data);
    }
    // wait data
    const response = await fetch(url, options);
    const data = await response.json();
    // put data in component attributes
    if (kwargs.attributes) {
        for (const [key, value] of Object.entries(attributes)) {
            this[key] = data[value];
        }
    }

    return data;
}
