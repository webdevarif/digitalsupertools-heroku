(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[495],{8740:function(e,r,a){(window.__NEXT_P=window.__NEXT_P||[]).push(["/register",function(){return a(5388)}])},6410:function(e,r,a){"use strict";var s=a(5893);a(7294);r.Z=function(e){var r=e.children;return(0,s.jsx)("div",{className:"account-body position-relative",children:(0,s.jsx)("div",{className:"account-body__inner flex min-h-screen items-center justify-center",children:(0,s.jsxs)("div",{className:"max-w-5xl border border-gray-200/50 w-full shadow-2xl shadow-gray-300/50 flex rounded-3xl overflow-hidden bg-white",children:[(0,s.jsx)("div",{className:"account-body__content w-2/5 p-6 lg:p-10",children:r}),(0,s.jsx)("div",{className:"account-body__banner bg-indigo-500 flex items-center justify-center w-3/5 p-6 lg:p-10",children:(0,s.jsxs)("div",{className:"account-body__banner-content text-white text-center",children:[(0,s.jsx)("h1",{className:"text-4xl mb-4",children:"Digital Supertools"}),(0,s.jsx)("p",{className:"mb-0",children:"A to Z supertools collections"})]})})]})})})}},5388:function(e,r,a){"use strict";a.r(r),a.d(r,{default:function(){return g}});var s=a(5893),t=a(7294),l=a(4416),n=a(5697),o=a.n(n),i=a(1163),c=a(124),d=a(9669),m=a.n(d),u=a(3454),p=a(6410),b=a(6893),h=a(5051);function x(e,r,a){return r in e?Object.defineProperty(e,r,{value:a,enumerable:!0,configurable:!0,writable:!0}):e[r]=a,e}var f=function(e){var r=e.register,a=(e.addEmail,e.isAuthenticated),l=(0,i.useRouter)(),n=(0,t.useState)({first_name:"",last_name:"",username:"",email:"",password:"",re_password:""}),o=n[0],c=n[1],d=o.first_name,m=o.last_name,u=o.username,f=o.email,g=o.password,y=o.re_password,j=(0,t.useState)(1),w=(j[0],j[1],(0,t.useState)(1)),N=(w[0],w[1],(0,t.useState)(1)),v=(N[0],N[1]),_=(0,t.useState)(1),k=(_[0],_[1]),P=(0,t.useState)(!1),C=(P[0],P[1],(0,t.useState)(1)),A=(C[0],C[1]),E=function(e){return c(function(e){for(var r=1;r<arguments.length;r++){var a=null!=arguments[r]?arguments[r]:{},s=Object.keys(a);"function"===typeof Object.getOwnPropertySymbols&&(s=s.concat(Object.getOwnPropertySymbols(a).filter((function(e){return Object.getOwnPropertyDescriptor(a,e).enumerable})))),s.forEach((function(r){x(e,r,a[r])}))}return e}({},o,x({},e.target.name,e.target.value)))},S={more:"Already have an Account?",label:{firstname:"First Name",lastname:"Last Name",email:"Your Email",username:"Username",password:"Password",re_password:"Confirm Password",submit:"Create Account"},links:{title:"Sign In",url:h.Z.url_login}},F=function(e){console.log(e),201!==e.status?(A(1),e.results.msg.username&&(v(3),console.log("username error")),e.results.msg.email&&(k(3),console.log("email error"))):(A(3),console.log("Created Account"),c({first_name:"",last_name:"",username:"",email:"",password:"",re_password:""}))};return a&&l.push("/"),(0,s.jsx)(p.Z,{children:(0,s.jsxs)("form",{onSubmit:function(e){console.log(o),e.preventDefault(),A(2),r(d,m,u,f,g,y,F)},children:[(0,s.jsxs)("div",{className:"form-heading mb-6",children:[(0,s.jsx)("h3",{className:"mb-1 text-2xl",children:"Register"}),(0,s.jsx)("p",{className:"text-sm text-gray-400",children:"We need some of your information to get started."})]}),(0,s.jsxs)("div",{className:"grid grid-cols-2 gap-4",children:[(0,s.jsxs)("div",{className:"form-group-grid mb-4",children:[(0,s.jsx)("label",{htmlFor:"form-first_name",className:"text-sm mb-2 block",children:S.label.firstname}),(0,s.jsx)("input",{type:"text",id:"form-first_name",placeholder:"First Name",name:"first_name",value:d,autoFocus:!0,onChange:E,required:!0,className:"bg-gray-50 rounded-md py-2 px-4 w-full border border-gray-200/50 placeholder:text-sm"})]}),(0,s.jsxs)("div",{className:"form-group-grid mb-3",children:[(0,s.jsx)("label",{htmlFor:"form-last_name",className:"text-sm mb-2 block",children:S.label.lastname}),(0,s.jsx)("input",{type:"text",id:"form-last_name",placeholder:"Last Name",name:"last_name",value:m,onChange:E,required:!0,className:"bg-gray-50 rounded-md py-2 px-4 w-full border border-gray-200/50 placeholder:text-sm"})]})]}),(0,s.jsxs)("div",{className:"form-group-grid mb-3",children:[(0,s.jsx)("label",{htmlFor:"form-username",className:"text-sm mb-2 block",children:S.label.username}),(0,s.jsx)("input",{type:"text",id:"form-username",placeholder:"Username",name:"username",value:u,onChange:E,required:!0,className:"bg-gray-50 rounded-md py-2 px-4 w-full border border-gray-200/50 placeholder:text-sm"})]}),(0,s.jsxs)("div",{className:"form-group-grid mb-3",children:[(0,s.jsx)("label",{htmlFor:"form-email",className:"text-sm mb-2 block",children:S.label.email}),(0,s.jsx)("input",{type:"email",id:"form-email",placeholder:"E-mail",name:"email",value:f,onChange:E,required:!0,className:"bg-gray-50 rounded-md py-2 px-4 w-full border border-gray-200/50 placeholder:text-sm"})]}),(0,s.jsxs)("div",{className:"form-group-grid mb-3",children:[(0,s.jsx)("label",{htmlFor:"form-password",className:"text-sm mb-2 block",children:S.label.password}),(0,s.jsxs)("div",{className:"relative",children:[(0,s.jsx)("input",{type:"Password",id:"form-password",name:"password",value:g,onChange:E,placeholder:"Password","aria-label":"Password","aria-describedby":"btnGroupPassword",className:"bg-gray-50 rounded-md py-2 px-4 w-full border border-gray-200/50 pr-10 placeholder:text-sm"}),(0,s.jsx)("span",{className:"absolute top-1/2 -translate-y-1/2 right-4 cursor-pointer",children:(0,s.jsx)(b.rDJ,{})})]})]}),(0,s.jsxs)("div",{className:"form-group-grid mb-3",children:[(0,s.jsx)("label",{htmlFor:"form-re_password",className:"text-sm mb-2 block",children:S.label.re_password}),(0,s.jsxs)("div",{className:"relative",children:[(0,s.jsx)("input",{type:"Password",id:"form-re_password",name:"re_password",value:y,onChange:E,placeholder:"Confirm Password","aria-label":"Confirm Password","aria-describedby":"btnGroupConfirmPassword",className:"bg-gray-50 rounded-md py-2 px-4 w-full border border-gray-200/50 pr-10 placeholder:text-sm"}),(0,s.jsx)("span",{className:"absolute top-1/2 -translate-y-1/2 right-4 cursor-pointer",children:(0,s.jsx)(b.rDJ,{})})]})]}),(0,s.jsxs)("div",{className:"form-check form-group mb-4",children:[(0,s.jsx)("input",{className:"form-check-input appearance-none h-4 w-4 border border-gray-300 rounded-sm bg-white checked:bg-blue-600 checked:border-blue-600 focus:outline-none transition duration-200 mt-1 align-top bg-no-repeat bg-center bg-contain float-left mr-2 cursor-pointer",type:"checkbox",value:"",id:"flexCheckDefault"}),(0,s.jsxs)("label",{className:"form-check-label text-gray-400 text-sm",htmlFor:"flexCheckDefault",children:["By creating an account you agree to ",(0,s.jsx)("a",{href:"#",className:"text-xs text-indigo-500",children:"the terms of use"})," and ",(0,s.jsx)("a",{href:"#",className:"text-xs text-indigo-500",children:"privacy policy"}),"."]})]}),(0,s.jsx)("div",{className:"form-group mb-4",children:(0,s.jsx)("button",{className:"py-2 px-4 bg-gradient-to-b from-indigo-500 to-indigo-700 text-gray-100 w-full rounded-md",children:S.label.submit})}),S.more&&(0,s.jsx)("div",{className:"more-links text-center",children:(0,s.jsxs)("p",{className:"mb-0 text-gray-400",children:[S.more," ",S.links&&(0,s.jsx)("a",{className:"text-indigo-500",href:S.links.url,children:S.links.title})]})})]})})};f.propTypes={register:o().func.isRequired,addEmail:o().func.isRequired,isAuthenticated:o().bool};var g=(0,l.$j)((function(e){return{isAuthenticated:e.auth.isAuthenticated}}),{register:c.z2,addEmail:function(e,r){return function(a){m().post("".concat(u.env.REACT_APP_API_URL,"/api/email/list"),e,{headers:{"Content-Type":"application/json",Authorization:(0,c.bQ)(),Accept:"application/json"}}).then((function(e){r({isValid:e.data.isValid,data:e})})).catch((function(e){r({isValid:!1,data:e.response})}))}}})(f)}},function(e){e.O(0,[806,774,888,179],(function(){return r=8740,e(e.s=r);var r}));var r=e.O();_N_E=r}]);