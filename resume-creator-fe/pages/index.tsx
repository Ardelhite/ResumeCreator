import type { NextPage } from 'next'
import {Button} from "@mui/material";
import {CommonLayout} from "../components/pages/CommonLayout";

const IndexPage: NextPage = () => {
  return(
      <CommonLayout>
          <Button>MUI TEST</Button>
      </CommonLayout>
  )
}

export default IndexPage
