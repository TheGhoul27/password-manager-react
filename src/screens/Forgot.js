import { useState} from 'react'
import { useHistory } from 'react-router-dom';
import {forgotPassword} from '../models'
import Form from "react-bootstrap/Form";
import Col from "react-bootstrap/Col";
import Button from "react-bootstrap/Button";
import { Link } from 'react-router-dom'
import Container from "react-bootstrap/Container";
import NavbarComponent from '../components/Navbar';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faUserCircle } from '@fortawesome/free-solid-svg-icons'
import { Flash } from '../components/Flash/flash';

export default function ForgotPassword() {

  const history = useHistory()
  if (localStorage.getItem('email')) {
    setTimeout(() => {
      window.flash('You are logged in', 'warning')
    }, 100)
    history.push('/') 
  }

  const [validated, setValidated] = useState(false);

  const handleSubmit = async (event) => {
    event.preventDefault();
    const body = {
      email: event.target.email.value
    }

    // Handle login logic

    if (!body.email) {
      setValidated(true);
    } else {
      const user = await forgotPassword(body.email)
      if (user) {
        //localStorage.setItem('email', body.email)
        localStorage.clear()
        history.push('/login');
        window.flash('Password sent successfully!', 'success')
      } else {
        window.flash('Invalid email', 'error')
      }
    }
  }

  return (
    <>
      <NavbarComponent />
      <Flash />
      <Container className='d-flex flex-column align-items-center justify-content-center' style={{ height: '80vh' }}>
        <p className="h3 display-4"><FontAwesomeIcon icon={faUserCircle} size="1x" /></p>
        <p className="h2 display-5">Forgot Password</p>
        <Form noValidate validated={validated} onSubmit={handleSubmit} style={{ minWidth: '300px' }}>
          <Form.Row>
            <Form.Group as={Col} md="12" controlId="validationCustom01">
              <Form.Label>Email</Form.Label>
              <Form.Control required name='email' type="email" placeholder="Email" />
              <Form.Control.Feedback type="invalid">Please provide a valid email.</Form.Control.Feedback>
              <Form.Control.Feedback>Looks Good!</Form.Control.Feedback>
            </Form.Group>
          </Form.Row>
          <Button type="submit">Forgot Password</Button>
          <p className="text-center"><Link to="/register">Register</Link> to create account!</p>
        </Form>
      </Container>
    </>
  )
}
