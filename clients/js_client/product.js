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
        console.log(() => response.data)
    }catch (error){
        console.error();
    }
}
handleUserPostRequest();

// const login = async () => {
//     try{
//         const token = btoa(testuser.username + ":" + testuser.password);
//         const config = {
//             headers: {"Authorization": "Basic " + token}
//         }
//         const response = await axios.post(baseURL + "api-auth/login/", config)
//         console.log("Login Succesfully!", response.data)
//     }catch(error){
//         console.error(error);
//     }
// }
// login();

const handleCategoryPostGetrequest = async () => {
    try{
        const categoryData = {
            name: "farming",
            description: "This is a farming category",
            tags: "farming tag"
        }
        await axios.post(baseURL + "api/products/categories/", categoryData);
        console.log(() => {
            message: "Categry POST completed successfully!"
        })

        const response = await axios.get(baseURL + "api/products/categories/" + "?" + `name=${categoryData.name}`);
        return response.data
    }catch(error){
        console.error();
    }
}

const product_data = {
    "title": "Test Product",
    "description": "This is a test product",
    "price": 3000.00,
    "summary": "This is a summary",
    "category": handleCategoryPostGetrequest(),
    "tags": "test, product, test product",
    "discount_type": "None",
    "discount_value": 0.0
}


axios.defaults.withCredentials = true;
const handleProductPostRequest = async () => {
    try{
        const response = await axios.post(baseURL + "api/products/", product_data);
        console.log(() => {
            status_code: response.status;
            data: response.data
        });
    }catch(error){
        console.error(error);
    }
}
handleProductPostRequest();


const handleDeleteProductRequest = 