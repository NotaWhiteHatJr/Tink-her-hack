import React from 'react';
import Item from '../Components/Item/Item';
import './Kids.css'
import all_product from '../Components/Assets/all_product';
const kid_products = all_product.filter((product) => {
    return product.category === "kid";
});

const Kids = () => {
    return (
        <div className="kids">
            <h1> POPULAR IN KIDS</h1>
            <hr/>
            {
                kid_products.map((item, i) => {
                    return <Item key={i} id={item.id} name={item.name} image= {item.image} new_price= {item.new_price} old_price={item.old_price}/>
                })
            }
        </div>
    );
};

export default Kids;