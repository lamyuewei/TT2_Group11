import { Form, Input, Button, Checkbox } from "antd";
import "antd/dist/antd.css";

const Login = ({ password, username, onClick }) => {
  const onFinish = (values) => {
    var Auth = false;
    let combinedDetails = { username, password };
    const value = JSON.stringify(values);
    // console.log(value);
    // console.log(combinedDetails);
    const isEqual = (combinedDetails, value) => {
      const combinedDetailsKeys = Object.keys(combinedDetails);
      const valueKeys = Object.keys(value);

      if (combinedDetailsKeys !== valueKeys) {
        return false;
      }

      for (let i of combinedDetailsKeys) {
        if (combinedDetails[i] !== value[i]) {
          return false;
        }
      }

      return true;
    };

    Auth = isEqual(combinedDetails, value);
    console.log(Auth);

    // if (
    //   values.password == { userPass } ||
    //   values.username == { userUserName }
    // ) {
    //   console.log("Success");
    // } else {
    //   console.log("Login failed");
    //   console.log({ userUserName }, { userPass });
    //   console.log(values);
    // }
  };

  const onFinishFailed = (errorInfo) => {
    console.log("Failed:", errorInfo);
  };

  return (
    <Form
      name="basic"
      labelCol={{
        span: 8,
      }}
      wrapperCol={{
        span: 16,
      }}
      onFinish={onFinish}
      onFinishFailed={onFinishFailed}
      autoComplete="off"
    >
      <Form.Item
        label="Username"
        name="username"
        rules={[
          {
            required: true,
            message: "Please input your username!",
          },
        ]}
      >
        <Input />
      </Form.Item>

      <Form.Item
        label="Password"
        name="password"
        rules={[
          {
            required: true,
            message: "Please input your password!",
          },
        ]}
      >
        <Input.Password />
      </Form.Item>

      <Form.Item
        wrapperCol={{
          offset: 8,
          span: 16,
        }}
      >
        <Button type="primary" htmlType="submit" onClick={onClick}>
          Submit
        </Button>
      </Form.Item>
    </Form>
  );
};

export default Login;
