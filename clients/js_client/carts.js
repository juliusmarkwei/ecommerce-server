import axios from "axios";
import assert from "assert";
import status from "statuses";


const baseURL = 'http://localhost:8000/';
export const getUser = async () => {
    try {
        const response = await axios.get(baseURL + "api/users/?username=julius");
        return response.data;
    } catch (error) {
        console.error('Error fetching user:', error);
        return null;
    }
}

const handleCartPOSTRequest = async () => {
    try {
        const userData = await getUser();
        if (!userData) {
            throw new Error('User data is undefined');
        }

        const username = userData.username;
        const token = btoa(username + ":" + "admin");
        const config = {
            headers: {
                Authorization: "Basic " + token
            }
        }
        const cartData = {
            status: "active"
        }
        const response = await axios.post(baseURL + "api/carts/", cartData, config);
        console.log('Cart POST response:', response.data);
    } catch (error) {
        console.error('Error in handleCartPOSTRequest:', error);
    }
}

handleCartPOSTRequest();


const handleCartGETRequest = async () => {
    try{
        const response = await axios.get(baseURL + "api/carts/?username=holmes");
        assert.equal(response.status, status('OK'));

    } catch (error) {
        console.error('Error in handleCartGETRequest:', error);
        return null;
    }
}
handleCartGETRequest();
