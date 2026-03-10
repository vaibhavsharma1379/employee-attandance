import { NavLink } from "react-router-dom";

const link =
    "block px-4 py-2 rounded-lg hover:bg-slate-700 transition";

export default function Sidebar() {
    return (
        <aside className="w-64 bg-slate-900 text-slate-200 p-6">
            <h1 className="text-xl font-bold mb-8">HRMS Lite</h1>

            <nav className="space-y-2">
                <NavLink to="/" className={link}>Dashboard</NavLink>
                <NavLink to="/employees" className={link}>Employees</NavLink>
                <NavLink to="/attendance" className={link}>Attendance</NavLink>
            </nav>
        </aside>
    );
}