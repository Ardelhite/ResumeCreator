import React, {ReactNode} from "react";
import {GeneralHeader} from "../heder/GeneralHeader";

// 全てのページの基本レイアウト
export const CommonLayout = (props: any) => {
    return (
        <div>
            <GeneralHeader/>
            {props.children}
        </div>
    )
}