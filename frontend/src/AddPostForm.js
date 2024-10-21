import React, { useState } from 'react';
import axios from 'axios';

function AddPostForm() {
  const [title, setTitle] = useState('');
  const [content, setContent] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();

    axios.post('http://localhost:8000/api/posts/', {
      title: title,
      content: content
    })
    .then(response => {
      console.log('Post added:', response.data);
      setTitle('');
      setContent('');
    })
    .catch(error => {
      console.error('Error adding post:', error);
    });
  };

  return (
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
  );
}

export default AddPostForm;
