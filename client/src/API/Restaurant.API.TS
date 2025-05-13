import axios from 'axios';

export const getRestaurants = async () => {
    
    try {
        const response = await axios.get('http://127.0.0.1:8000/Rest/api/v1/restaurants/');
        return response.data;
    } catch (error) {
        console.error('Error', error);
        throw error;
    }
}