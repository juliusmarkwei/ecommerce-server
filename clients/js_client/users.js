//testing users CRUD

import axios from 'axios'

export const baseURL = 'http://localhost:8000/'
const testuser1 = {
    "username": "testuser1",
    "email": "ulooza@wice.pm",
    "first_name": "Cole",
    "last_name": "Harris",
    "password": "12345678",
    "phone": "test123",
    // "is_active": true,
}

const testuser2 = {
    "username": "testuser2",
    "email": "haldot@sise.pm",
    "first_name": "Hal",
    "last_name": "Dot",
    "password": "test123",
    "phone": "(259) 873-9769"
}

const testuser3 = {
    "username": "testuser3",
    "email": "esrodnu@piwoz.ml",
    "first_name": "Clayton",
    "last_name": "Abbott",
    "password": "test123",
    "phone": "(739) 740-1265"
}

//  adding user to database
const user1 = axios.post(baseURL + "api/users/", testuser1).then(
    (response) => {console.log(response.status)}
).catch((error) => {
    console.error(error)
    }
).finally(() => console.log("POST request completed!"))


const user2 = axios.post(baseURL + "api/users/", testuser2).then(
    (response) => {console.log(response.status)}
).catch((error) => {
    console.error(error)
    }
).finally(() => console.log("POST request completed!"))


const user3 = axios.post(baseURL + "api/users/", testuser3).then(
    (response) => {console.log(response.status)}
).catch((error) => {
    console.error(error)
    }
).finally(() => console.log("POST request completed!"))


// delete a user
axios.delete(baseURL + "api/users/" + "?" + "username=Ara.Senger").then(
    (response) => {
        console.log(response.status)
    }
).catch(
    (error) => {
        console.error(error)
    }
).finally(() => console.log("DELETE request completed!"))

// get a user
axios.get(baseURL + "api/users/").then(
    (response) => {
        console.log({"data": response.data.slice(0, 2)})
    }
).catch(
    (error) => {
        console.error(error)
    }
).finally(() => console.log("GET request completed!"))

