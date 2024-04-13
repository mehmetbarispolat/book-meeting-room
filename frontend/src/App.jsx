import React, { useState } from 'react';
import './App.css';
import BookingForm from './components/BookingForm';
import RoomList from './components/RoomList';

function App() {
  const [searchParams, setSearchParams] = useState(null);

  const handleSearch = (attendees, timeframe) => {
    setSearchParams({ attendees, timeframe });
  };

  return (
    <div className="App">
      <h1>Meeting Room Booking</h1>
      <BookingForm onSearch={handleSearch} />
      {searchParams && <RoomList {...searchParams} />}
    </div>
  );
}

export default App;
