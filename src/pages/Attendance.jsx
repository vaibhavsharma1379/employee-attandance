import { useEffect, useState } from "react";
import api from "../api/client";

export default function Attendance() {
    const [emps, setEmps] = useState([]);
    const [form, setForm] = useState({
        employee:"", date:"", status:"Present"
    });

    useEffect(()=>{
        api.get("/api/employees/").then(res =>
            setEmps(res.data.results || res.data)
        );
    },[]);

    const submit = async e => {
        e.preventDefault();
        await api.post("/api/attendance/", form);
        alert("Attendance marked");
    };

    return (
        <div>
            <h1 className="text-2xl font-bold mb-6">Mark Attendance</h1>

            <form onSubmit={submit}
                  className="bg-white p-6 rounded-xl shadow-sm border max-w-xl space-y-4">

                <select className="input"
                        onChange={e=>setForm({...form,employee:e.target.value})}>
                    <option>Select Employee</option>
                    {emps.map(e=>(
                        <option key={e.id} value={e.id}>
                            {e.full_name} ({e.employee_id})
                        </option>
                    ))}
                </select>

                <input type="date" className="input"
                       onChange={e=>setForm({...form,date:e.target.value})}/>

                <select className="input"
                        onChange={e=>setForm({...form,status:e.target.value})}>
                    <option>Present</option>
                    <option>Absent</option>
                </select>

                <button className="bg-slate-900 text-white px-6 py-2 rounded-lg">
                    Submit
                </button>
            </form>
        </div>
    );
}