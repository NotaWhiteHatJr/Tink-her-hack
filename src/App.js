
import './App.css';
import Navbar from './Components/Navbar/Navbar';
import { BrowserRouter,Routes,Route } from 'react-router-dom';

import Cart from './Pages/Cart';
import LoginSignup from './Pages/LoginSignup';
import Product from './Pages/Product';
import Shop from './Pages/Shop';
import Men from './Pages/Men';
import Women from './Pages/Women';
import Kids from './Pages/Kids';
function App() {
  return (
    <div >
       <BrowserRouter>
      <Navbar/>
      
      <Routes>
        <Route path="/" element ={<Shop/>}/>
        <Route path="/men" element ={<Men/>}/>
         <Route path="/women" element ={<Women/>}/>
       <Route path="/kids" element ={<Kids/>}/> 
        <Route path="/product" element={<Product/>}>
        <Route path=":productId" element={<Product/>}/>
      </Route>
      <Route path="/cart" element={<Cart/>}/>
      <Route path="/login" element={<LoginSignup/>}/>
      </Routes>
      </BrowserRouter>
      
    </div>
  );
}

export default App;
