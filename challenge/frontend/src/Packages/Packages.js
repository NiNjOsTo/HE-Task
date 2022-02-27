import "bootstrap/dist/css/bootstrap.css"
import "./Packages.css"
import axios from "axios"
import React, { useState,useEffect }  from 'react';
import { Link } from "react-router-dom";

let Packages = () => {
    const [packagesList, setpackagesList] = useState([]);
    const [Loading, setLoading] = useState(true);
    const [NextPG, setNextPG] = useState();
    let getPackages = () => {
        axios
          .get("Packages/?format=json")
            .then((res) => {
                setpackagesList(res.data.results);
                setNextPG(res.data.next);
                console.log(res.data.results);
                setLoading(false);
          })
          .catch((err) => console.log(err));
    };
    useEffect(() => {
        getPackages();
    }, []);
    // - Title
    // - Agency Name
    // - Country Name
    // - Active status 
    // - sold out status
    let RenderItems = () => {
            return Loading ? <h1>Loading</h1> :
                packagesList.map((item) => (
                    <tr key={item.id}>
                        <td className="no">
                                {item.id}    
                        </td>
                        <td className="text-left">
                            <Link to={"/package/"+item.id} ><h3>{item.title}</h3></Link>
                            
                            {item.agency.name}
                        </td>
                        <td className="unit">{item.country.name}</td>
                        <td className="qty">{item.is_active?"Active Package":"Package not active"}</td>
                        <td className="total">{item.mark_as_sold_out?"Sold Out":"In Stock"}</td>
                    </tr>
                ));
        
    };
    return (
        <div className="container">
            <div className="card">
                <div className="card-body">
                            <div id="invoice">
                                <div className="invoice overflow-auto">
                                    <div>
                                <main>
                                    <table>
                                        <thead>
                                            <tr>
                                                <th>#</th>
                                                <th className="text-left">Title ,
                                                Agency
                                                </th>
                                                <th className="text-right">Country</th>
                                                <th className="text-right">Active Status</th>
                                                <th className="text-right">Sold Status</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            <RenderItems />
                                        </tbody>
                                    </table>
                                </main>
                                <footer>Hello Explorer Task.</footer>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}
export default Packages;