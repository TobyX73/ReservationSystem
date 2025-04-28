import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import RestaurantPage from "./pages/RestaurantPage";
import RestaurantFormPage from "./pages/RestaurantFormPage";
import Navigation from "./components/Navigation";

function App() {
  return (
    <BrowserRouter>
      <Navigation />
      <Routes>
        <Route path="/" element={<Navigate to="/restaurant" />} />
        <Route path="/Restaurant" element={<RestaurantPage />} />
        <Route path="/Restaurant-create" element={<RestaurantFormPage />} />
      </Routes>
    </BrowserRouter>
  );
}
 
export default App;