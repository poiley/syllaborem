import React from "react";
import GitHubLogin from "react-github-login";

const GithubLoginButton = props => {
  const onSuccess = response => {
    console.log(response);
    props.sendGithubCode(response);
  };
  const onFailure = response => console.error(response);
  return (
    <GitHubLogin
      clientId="98eeeb46a8da92535b9d"
      onSuccess={onSuccess}
      onFailure={onFailure}
      redirectUri=""
      buttonText="Login with Github"
      className="fa fa-github btn btn-primary"
    />
  );
};

export default GithubLoginButton;
