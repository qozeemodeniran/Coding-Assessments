function fetchDataWithPromise() {
    return new Promise((resolve, reject) => {
        fetch('https://jsonplaceholder.typicode.com/posts/1')
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                resolve(data);
            })
            .catch(error => {
                reject(error);
            });
    });
}
// Usage
fetchDataWithPromise()
    .then(data => {
        console.log('Data fetched with promise:', data);
    })
    .catch(error => {
        console.error('Error fetching data with promise:', error);
    });