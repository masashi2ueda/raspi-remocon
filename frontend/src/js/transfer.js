// import axios from 'axios'
const axios = require('axios');

function send_sig(baseURL, deviceName){
    console.log(deviceName);
    axios.create({baseURL:baseURL}).
    get('/api/trans-sig', {
        params: {
            device_name: deviceName,
        }
    }).then(function (response) {
        console.log(response.data);
    });
}

export default send_sig;
