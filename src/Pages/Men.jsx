import React from 'react';
import './Men.css'
import Item from '../Components/Item/Item';
import new_collections from "../Components/Assets/new_collections"
const Men = () => {
    return (
        <div className="men">
            <h1> POPULAR IN MEN</h1>
            <hr/>
        {new_collections.map((item,i)=>{
            return <Item key={i} id={item.id} name={item.name} image= {item.image} new_price= {item.new_price} old_price={item.old_price}/>
        })}
    </div>
    );
};

export default Men;