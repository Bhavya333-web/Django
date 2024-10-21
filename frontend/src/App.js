import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [posts, setPosts] = useState([]);

  // Fetch posts from Django API when component mounts
  useEffect(() => {
    axios.get('http://localhost:8000/api/posts/')
      .then(response => {
        setPosts(response.data);  // Set posts data
      })
      .catch(error => {
        console.error("There was an error fetching the posts!", error);
      });
  }, []);

  return (
    <div className="App">
      <h1>Blog Posts</h1>
      <ul>
        {posts.map(post => (
          <li key={post.id}>
            <h2>{post.title}</h2>
            <p>{post.content}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
