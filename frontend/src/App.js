import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [posts, setPosts] = useState([]);  // Blog posts
  const [title, setTitle] = useState('');  // New post title
  const [content, setContent] = useState('');  // New post content

  // Fetch posts from Django API
  useEffect(() => {
    axios.get('http://localhost:8000/api/posts/')
      .then(response => {
        setPosts(response.data);  // Set posts data
      })
      .catch(error => {
        console.error("There was an error fetching the posts!", error);
      });
  }, []);

  // Handle form submission to create a new blog post
  const handleSubmit = (event) => {
    event.preventDefault();

    axios.post('http://localhost:8000/api/posts/', {
      title: title,
      content: content
    })
    .then(response => {
      setPosts([...posts, response.data]);  // Update the post list with the new post
      setTitle('');  // Clear form fields
      setContent('');
    })
    .catch(error => {
      console.error("There was an error creating the post!", error);
    });
  };

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

      <h2>Add a New Post</h2>
      <form onSubmit={handleSubmit}>
        <input 
          type="text" 
          placeholder="Title" 
          value={title}
          onChange={(e) => setTitle(e.target.value)}
        />
        <textarea 
          placeholder="Content" 
          value={content}
          onChange={(e) => setContent(e.target.value)}
        />
        <button type="submit">Add Post</button>
      </form>
    </div>
  );
}

export default App;
