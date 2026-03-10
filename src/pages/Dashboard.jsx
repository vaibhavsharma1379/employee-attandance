import { useEffect, useState } from "react";
import api from "../api/client";

export default function Dashboard() {
    const [stats, setStats] = useState(null);

    useEffect(() => {
        api.get("/api/dashboard/").then(res => setStats(res.data));
    }, []);

    if (!stats) return <div>Loading...</div>;

    return (
        <div>
            <h1 className="text-2xl font-bold mb-6">Dashboard</h1>

            <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                <StatCard title="Total Employees" value={stats.total_employees} />
                <StatCard title="Present Today" value={stats.present_today} />
                <StatCard title="Absent Today" value={stats.absent_today} />
            </div>
        </div>
    );
}

function StatCard({ title, value }) {
    return (
        <div className="bg-white p-6 rounded-xl shadow-sm border">
            <p className="text-slate-500 text-sm">{title}</p>
            <h2 className="text-3xl font-bold mt-2">{value}</h2>
        </div>
    );
}