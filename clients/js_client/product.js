//testing product CRUD
import axios  from "axios";

const baseURL = "http://localhost:8000/";
const testuser = {
    "username": "febja.modarmi",
    "password": "test123",
    "email": "ismejdoh@gaazlar.sm",
    "first_name": "Febja",
    "last_name": "Modarmi",
    "phone": "+0771234567",
};

const handleUserPostRequest = async () => {
    try{
        const response = await axios.post(baseURL + "api/users/", testuser);
        console.log(() => response.status)
    }catch (error){
        console.error(error);
    }
}
handleUserPostRequest();

const login = async () => {
    try{
        const token = btoa(testuser.username + ":" + testuser.password);
        const config = {
            headers: {"Authorization": "Basic " + token}
        }
        const response = await axios.post(baseURL + "api-auth/login/", config)
        console.log("Login Succesfully!", response.data)
    }catch(error){
        console.error(error);
    }
}
login();

const product_data = {
    "title": "Test Product",
    "description": "This is a test product",
    "price": 3000.00,
    "summary": "This is a summary",
    "category": 1,
    "tags": "test, product, test product",
    "discount_type": "None",
    "discount_value": 0.0
}


axios.defaults.withCredentials = true;
const handleProductPostRequest = async () => {
    try{
        const response = await axios.post(baseURL + "api/products/", product_data);
        console.log(() => response.status);
    }catch(error){
        console.error(error);
    }
}
handleProductPostRequest();