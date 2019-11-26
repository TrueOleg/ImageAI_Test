import fetch from 'isomorphic-fetch';


const BASE_API_URL = "http://localhost:5000/api/image"

export function api(api_end_point, data) {

    return fetch(BASE_API_URL,
        {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        }).then((response) => {
            console.log('res', response);
            return response.body;
        });
}