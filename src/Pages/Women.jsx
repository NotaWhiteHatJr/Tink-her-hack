import React from 'react';
import Item from '../Components/Item/Item';
import './Women.css'
import data_product from "../Components/Assets/data";
const Women = () => {
    return (
        <div className="women">
            <h1> POPULAR IN WOMEN</h1>
            <hr/>
        {data_product.map((item,i)=>{
            return <Item key={i} id={item.id} name={item.name} image= {item.image} new_price= {item.new_price} old_price={item.old_price}/>
        })}
    </div>
    );
};

export default Women;