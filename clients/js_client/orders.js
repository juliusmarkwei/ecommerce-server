//testing orders CRUD
import axios from 'axios';
import assert from 'assert';
import status from 'statuses';


const baseURL = 'http://localhost:8000/';
const getUser = async () => {
    try {
        const response = await axios.get(baseURL + "api/users/?username=julius");
        return response.data;
    } catch (error) {
        console.error('Error fetching user:', error);
        return null;
    }
}

const handleOodersPOSTRequest = async () => {
    try {
        const userData = await getUser();
        if (!userData) {
            throw new Error('User data is undefined');
        }
        const config = {
            headers: { // I used the admin credentils I created for myself
                Authorization: 'Basic' + btoa(userData.username + ':' + 'admin')
            }
        }
        const response = await axios.post(baseURL + '/orders/', config= config);
        console.log('Orders sent successfully!');
        assert.equal(response.status, status('CREATED'));
        return response.data;

    }catch (error) {
        console.error('Error in handleOrdersPOSTRequest:', error);
        return null;
    }
}
handleOodersPOSTRequest();

console.log('Testing orders CRUD...');