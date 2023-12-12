//testing product CRUD
import axios  from "axios";


const baseURL = 'http://localhost:8000/';
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
        console.error(error);
    }
}
handleUserPostRequest();


const handleCategoryPostGetrequest = async () => {
    try{
        const categoryData = {
            name: "farming",
            description: "This is a farming category",
            tags: "farming tag"
        }
        await axios.post(baseURL + "api/products/categories/", categoryData);
        console.log({
            message: "Categry POST completed successfully!"
        })

        const response = await axios.get(baseURL + "api/products/categories/" + "?" + `name=${categoryData.name}`);
        return response.data
    }catch(error){
        console.error(error);
    }
}
handleCategoryPostGetrequest();


const product_data1 = {
    "title": "Test Product 1",
    "description": "This is a test product 1",
    "price": 3000.00,
    "summary": "This is a summary 1",
    "category": 7,
    "tags": "test, product, test product",
    "discount_type": None,
    "discount_value": 0.0
}

const product_data2 = {
    "title": "Test Product 2",
    "description": "This is a test product",
    "price": 1400.00,
    "summary": "This is a summary",
    "category": 3,
    "tags": "test, product, test product",
    "discount_type": None,
    "discount_value": 0.0
}


axios.defaults.withCredentials = true;
const handleProductPostRequest = async (product_data) => {
    try{
        const response = await axios.post(baseURL + "api/products/", product_data);
        console.log({
            status_code: response.status,
            data: response.data
        });
    }catch(error){
        console.error(error);
    }
}
handleProductPostRequest(product_data1);
handleProductPostRequest(product_data2);


const handleDeleteProductRequest = async () => {
    try{
        await axios.delete(baseURL + "api/products" + "?" + "title=" + product_data1.title);
        console.log({
            message: "Product deleted successfully!"
        })
    }catch(error){
        console.error(error);
    }
}
handleDeleteProductRequest();