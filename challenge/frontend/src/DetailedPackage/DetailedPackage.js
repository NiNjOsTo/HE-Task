import React, { useEffect,useState } from "react";
import "./DetailedPackage.css"
import { useParams } from "react-router-dom";
import axios from "axios";
const DetailedPackage = () => {
    const { id } = useParams();
    const [pack, setPack] = useState([]);
    const [Loading, setLoading] = useState(true);
    const [FutureDate, setFutureDate] = useState(false);
    let getPackage = () => {
        axios
          .get("/Packages/"+id+"/?format=json")
            .then((res) => {
                setPack(res.data);
                console.log(res.data);
                setLoading(false);
          })
          .catch((err) => console.log(err));
    };
    useEffect(() => {
        getPackage();
    }, []);
    let compareDates = (element) => {
        let objs = element.dates.filter((date) => new Date(date.date) >  new Date("2020-06-30"))
        return objs.length;
    }

    //// the problem is that the dates are not filtered correctly
    let RenderVariants = () => {
        return Loading ? <h1>Loading</h1> : pack.variants.map(element => {
            setFutureDate(false);
            return (
                <tr>
                    <td className="no">
                        {element.title}
                    </td>
                    <td className="text-left">
                        <h3>{
                            compareDates(element) > 0 ? "Has Future Dates" :  "No Future Dates"
                        }</h3>
                    </td>
                    <td className="unit">{element.mark_as_sold_out ? "Sold Out" : "In Stock"}</td>
                </tr>
            )
        },
        )
    }
    return (
        <div>

        <div className="jumbotron">
            <h1 className="display-3" >{pack.title}</h1>
        </div>
            <div className="container">
            <div className="card">
                <div className="card-body">
                            <div id="invoice">
                                <div className="invoice overflow-auto">
                                <main>
                                    <table>
                                        <thead>
                                            <tr>
                                                <th>Title</th>
                                                <th className="text-left">Future Dates</th>
                                                <th className="text-right">Status</th>
                                            </tr>
                                        </thead>
                                            <tbody>
                                                {Loading ? <h1>loassding</h1> : <RenderVariants />}
                                           {/* <RenderVariants /> */}
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
    );
};
  export default DetailedPackage