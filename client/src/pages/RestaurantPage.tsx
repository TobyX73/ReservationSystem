import RestaurantList from '../components/RestaurantList';
import { useEffect } from 'react'; 

export default function RestaurantPage() {
    useEffect(() => {
        console.log("Restaurant Page");
    }, []);

    return (
        <div>
            <RestaurantList />
        </div>
    )
}