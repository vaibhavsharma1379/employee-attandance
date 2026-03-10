import { useEffect, useState } from "react";
import api from "../api/client";

export default function Employees() {
    const [employees, setEmployees] = useState([]);
    const [form, setForm] = useState({
        employee_id: "", full_name: "", email: "", department: ""
    });

    const load = () =>
        api.get("/api/employees/").then(res =>
            setEmployees(res.data.results || res.data)
        );

    useEffect(()=>{
        load()
    }, []);

    const submit = async e => {
        e.preventDefault();
        await api.post("/api/employees/", form);
        setForm({ employee_id:"", full_name:"", email:"", department:"" });
        load();
    };

    const remove = async id => {
        await api.delete(`/api/employees/${id}/`);
        load();
    };

    return (
        <div>
            <h1 className="text-2xl font-bold mb-6">Employees</h1>

            {/* Form */}
            <form onSubmit={submit}
                  className="bg-white p-6 rounded-xl shadow-sm border mb-6">
                <div className="grid md:grid-cols-4 gap-4">
                    <Input placeholder="Employee ID"
                           value={form.employee_id}
                           onChange={v=>setForm({...form,employee_id:v})}/>
                    <Input placeholder="Full Name"
                           value={form.full_name}
                           onChange={v=>setForm({...form,full_name:v})}/>
                    <Input placeholder="Email"
                           value={form.email}
                           onChange={v=>setForm({...form,email:v})}/>
                    <Input placeholder="Department"
                           value={form.department}
                           onChange={v=>setForm({...form,department:v})}/>
                </div>

                <button className="mt-4 bg-slate-900 text-white px-6 py-2 rounded-lg">
                    Add Employee
                </button>
            </form>

            {/* Table */}
            <div className="bg-white rounded-xl shadow-sm border overflow-hidden">
                <table className="w-full">
                    <thead className="bg-slate-50 text-left">
                    <tr>
                        <Th>ID</Th><Th>Name</Th><Th>Email</Th><Th>Dept</Th><Th/>
                    </tr>
                    </thead>
                    <tbody>
                    {employees.map(e => (
                        <tr key={e.id} className="border-t">
                            <Td>{e.employee_id}</Td>
                            <Td>{e.full_name}</Td>
                            <Td>{e.email}</Td>
                            <Td>{e.department}</Td>
                            <Td>
                                <button onClick={()=>remove(e.id)}
                                        className="text-red-600 hover:underline">
                                    Delete
                                </button>
                            </Td>
                        </tr>
                    ))}
                    </tbody>
                </table>
            </div>
        </div>
    );
}

const Input = ({placeholder,value,onChange}) => (
    <input
        className="border rounded-lg px-3 py-2 w-full"
        placeholder={placeholder}
        value={value}
        onChange={e=>onChange(e.target.value)}
    />
);

const Th = ({children}) => (
    <th className="px-4 py-3 text-sm font-semibold">{children}</th>
);

const Td = ({children}) => (
    <td className="px-4 py-3 text-sm">{children}</td>
);