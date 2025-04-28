import { Link } from "react-router-dom";

export default function RestaurantList() {
    return (
        <>
            <h1>Restaurant List</h1>
            <ul>
                <li>
                    <Link to="/restaurant/1">Restaurant 1</Link>
                </li>
                <li>
                    <Link to="/restaurant/2">Restaurant 2</Link>
                </li>
                <li>
                    <Link to="/restaurant/3">Restaurant 3</Link>
                </li>
            </ul>
        </>
    );
}