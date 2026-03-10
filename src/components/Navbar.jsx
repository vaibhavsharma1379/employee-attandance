import { Link } from "react-router-dom";

export default function Navbar() {
    return (
        <nav style={nav}>
            <h2>HRMS Lite</h2>
            <div>
                <Link to="/">Dashboard</Link>
                <Link to="/employees">Employees</Link>
                <Link to="/attendance">Attendance</Link>
            </div>
        </nav>
    );
}

const nav = {
    display: "flex",
    justifyContent: "space-between",
    padding: "16px 24px",
    background: "#0f172a",
    color: "white",
};