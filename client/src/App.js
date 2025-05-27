import React, { useEffect, useState } from 'react';
import axios from 'axios';
import {
  BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer,
  LineChart, Line, PieChart, Pie, Cell, Legend
} from 'recharts';
import {
  Select, MenuItem, FormControl, InputLabel,
  Grid, Card, CardContent, Typography, Button
} from '@mui/material';

const API_BASE = 'http://localhost:8000/api';
const COLORS = ['#FFBB28', '#00C49F', '#0088FE', '#FF8042', '#FF6384', '#36A2EB'];

const EDAApp = () => {
  const [filters, setFilters] = useState({
    brand: 'All',
    packType: 'All',
    ppg: 'All',
    channel: 'All',
    year: 'All'
  });

  const [options, setOptions] = useState({
    brands: [],
    pack_types: [],
    ppgs: [],
    channels: [],
    years: []
  });

  const [salesValue, setSalesValue] = useState([]);
  const [volumeData, setVolumeData] = useState([]);
  const [yearlyValue, setYearlyValue] = useState([]);
  const [monthlyTrend, setMonthlyTrend] = useState([]);
  const [marketShare, setMarketShare] = useState([]);

  const fetchFilters = async () => {
    const res = await axios.get(`${API_BASE}/filters/`);
    setOptions(res.data);
  };

  const fetchData = async () => {
    const params = {};
    for (const key in filters) {
      if (filters[key] !== 'All') {
        params[key] = filters[key];
      }
    }
    const res = await axios.get(`${API_BASE}/dashboard-data/`, { params });
    setSalesValue(res.data.salesValue);
    setVolumeData(res.data.volumeContribution);
    setYearlyValue(res.data.yearlyValue);
    setMonthlyTrend(res.data.monthlyTrend);
    setMarketShare(res.data.marketShare);
  };

  useEffect(() => {
    fetchFilters();
  }, []);

  useEffect(() => {
    fetchData();
  }, [filters]);

  const handleChange = (e) => {
    setFilters({ ...filters, [e.target.name]: e.target.value });
  };

  const resetFilters = () => {
    setFilters({
      brand: 'All',
      packType: 'All',
      ppg: 'All',
      channel: 'All',
      year: 'All'
    });
  };

  return (
    <div style={{ padding: 32, background: '#f7f9fb', minHeight: '100vh' }}>
      <Typography variant="h4" gutterBottom>EDA Dashboard</Typography>

      {/* Filters */}
      <Grid container spacing={2}>
        {[
          { label: 'Brand', name: 'brand', values: options.brands },
          { label: 'Pack Type', name: 'packType', values: options.pack_types },
          { label: 'PPG', name: 'ppg', values: options.ppgs },
          { label: 'Channel', name: 'channel', values: options.channels },
          { label: 'Year', name: 'year', values: options.years }
        ].map(({ label, name, values }) => (
          <Grid item xs={12} sm={2.4} key={name}>
            <FormControl fullWidth>
              <InputLabel>{label}</InputLabel>
              <Select
                name={name}
                value={filters[name]}
                onChange={handleChange}
                label={label}
              >
                <MenuItem value="All">All</MenuItem>
                {values.map((val) => (
                  <MenuItem key={val} value={val}>{val}</MenuItem>
                ))}
              </Select>
            </FormControl>
          </Grid>
        ))}

        <Grid item xs={12} sm={2}>
          <Button variant="outlined" fullWidth onClick={resetFilters}>Reset</Button>
        </Grid>
      </Grid>

      {/* Charts */}
      <Grid container spacing={4} style={{ marginTop: 30 }}>
        {/* Sales Value */}
        <Grid item xs={12} md={6}>
          <Card>
            <CardContent>
              <Typography variant="h6" gutterBottom>Sales Value (EURO)</Typography>
              <ResponsiveContainer width="100%" height={250}>
                <BarChart layout="vertical" data={salesValue}>
                  <XAxis type="number" label={{ value: 'Value', position: 'insideBottom', offset: -5 }} />
                  <YAxis dataKey="year" type="category" label={{ value: 'Year', angle: -90, position: 'insideLeft' }} />
                  <Tooltip />
                  <Bar dataKey="value" fill="#00C49F" />
                </BarChart>
              </ResponsiveContainer>
            </CardContent>
          </Card>
        </Grid>

        {/* Volume Contribution */}
        <Grid item xs={12} md={6}>
          <Card>
            <CardContent>
              <Typography variant="h6" gutterBottom>Volume Contribution (lbs)</Typography>
              <ResponsiveContainer width="100%" height={250}>
                <BarChart layout="vertical" data={volumeData}>
                  <XAxis type="number" label={{ value: 'Volume', position: 'insideBottom', offset: -5 }} />
                  <YAxis dataKey="brand" type="category" label={{ value: 'Brand', angle: -90, position: 'insideLeft' }} />
                  <Tooltip />
                  <Bar dataKey="volume" fill="#FFBB28" />
                </BarChart>
              </ResponsiveContainer>
            </CardContent>
          </Card>
        </Grid>

        {/* Yearly Value */}
        <Grid item xs={12} md={6}>
          <Card>
            <CardContent>
              <Typography variant="h6" gutterBottom>Year-wise Value</Typography>
              <ResponsiveContainer width="100%" height={250}>
                <BarChart data={yearlyValue}>
                  <XAxis dataKey="year" label={{ value: 'Year', position: 'insideBottom', offset: -5 }} />
                  <YAxis label={{ value: 'Value', angle: -90, position: 'insideLeft' }} />
                  <Tooltip />
                  <Bar dataKey="value" fill="#0088FE" />
                </BarChart>
              </ResponsiveContainer>
            </CardContent>
          </Card>
        </Grid>

        {/* Monthly Trend */}
        <Grid item xs={12} md={6}>
          <Card>
            <CardContent>
              <Typography variant="h6" gutterBottom>Monthly Trend (Value)</Typography>
              <ResponsiveContainer width="100%" height={250}>
                <LineChart data={monthlyTrend}>
                  <XAxis dataKey="month" label={{ value: 'Month', position: 'insideBottom', offset: -5 }} />
                  <YAxis label={{ value: 'Value', angle: -90, position: 'insideLeft' }} />
                  <Tooltip />
                  <Line type="monotone" dataKey="value" stroke="#FF8042" strokeWidth={2} />
                </LineChart>
              </ResponsiveContainer>
            </CardContent>
          </Card>
        </Grid>

        {/* Market Share */}
        <Grid item xs={12} md={6}>
          <Card>
            <CardContent>
              <Typography variant="h6" gutterBottom>Market Share</Typography>
              <ResponsiveContainer width="100%" height={250}>
                <PieChart>
                  <Pie
                    data={marketShare}
                    dataKey="share"
                    nameKey="brand"
                    outerRadius={100}
                    label
                  >
                    {marketShare.map((entry, index) => (
                      <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                    ))}
                  </Pie>
                  <Legend />
                  <Tooltip />
                </PieChart>
              </ResponsiveContainer>
            </CardContent>
          </Card>
        </Grid>
      </Grid>
    </div>
  );
};

export default EDAApp;
