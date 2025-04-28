import { Link } from "react-router-dom";

export default function Navigation() {
    return (
        <>
            <Link to="/Restaurant">
                <h1>Restaurant</h1>
            </Link>
            <Link to="/Restaurant-create">
                <h1>Add Restaurant</h1>
            </Link>
        </>
    );
}