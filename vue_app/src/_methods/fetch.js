
async function fetchApi(url, kwargs, logout = false, method = "GET") {

    let options = {
        method: method,
        headers: {
            'Content-Type': 'application/json',
        }
    }
    if (logout) {
        url = `http://log:out@127.0.0.1:8080`
    }

    const response = await fetch(url, options);
    const data = await response.json();

    for (const [key, value] of Object.entries(kwargs)) {
        this[key] = data[value];
    }

    return data;
}

export default fetchApi
