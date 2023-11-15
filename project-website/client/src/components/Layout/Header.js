import Button from "react-bootstrap/Button";
import Container from "react-bootstrap/Container";
import Form from "react-bootstrap/Form";
import Nav from "react-bootstrap/Nav";
import Navbar from "react-bootstrap/Navbar";
import NavDropdown from "react-bootstrap/NavDropdown";
import styles from "./Header.module.css";

const Header = (props) => {
  return (
    <Navbar
      expand="lg"
      className={`bg-body-tertiary ${styles[props.className]}`}
      fixed="top"
      // bg="dark"
      // data-bs-theme="dark"
    >
      <Container fluid>
        <Navbar.Brand href="#">
          <img
            src="https://flowbite.com/docs/images/logo.svg"
            alt="Flowbite Logo"
          />
          <span>City of Williamston</span>
        </Navbar.Brand>
        <Navbar.Toggle aria-controls="navbarScroll" />
        <Navbar.Collapse id="navbarScroll">
          <Nav
            className="me-auto my-2 my-lg-0"
            style={{ maxHeight: "100px" }}
            navbarScroll
          >
            <Nav.Link href="#action1">Home</Nav.Link>
            <Nav.Link href="#action2">Boards & Commissions</Nav.Link>
            <NavDropdown title="Departments" id="navbarScrollingDropdown">
              <NavDropdown.Item href="#action3">
                Police Department
              </NavDropdown.Item>
              <NavDropdown.Item href="#action4">Water & Sewer</NavDropdown.Item>
              <NavDropdown.Divider />
              {/* <NavDropdown.Item href="#action5">
                Something else here
              </NavDropdown.Item> */}
            </NavDropdown>
            <Nav.Link href="#" disabled>
              Link
            </Nav.Link>
          </Nav>
          <Form className="d-flex">
            <Form.Control
              type="search"
              placeholder="Search"
              className="me-2"
              aria-label="Search"
            />
            <Button variant="outline-success">Search</Button>
          </Form>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
};

export default Header;
