from django.urls import path,include,re_path
from.import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve
from .views import EmailAttachementView, save_data

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('base', views.base, name='base'),
    path('logout', views.logout, name='logout'),
    path('view_profile', views.view_profile, name='view_profile'),
    path('edit_profile/<pk>', views.edit_profile, name='edit_profile'),
    path('itemview',views.itemview,name='itemview'),
    path('additem',views.additem,name='additem'),
    path('add',views.add,name='add'),
    path('add_account',views.add_account,name='add_account'),
    path('detail/<int:id>',views.detail,name='detail'),
    path('edititem/<int:id>',views.edititem,name='edititem'),
    path('edit_db/<int:id>',views.edit_db,name='edit_db'),
    path('Action/<int:id>',views.Action,name='Action'),
    path('cleer/<int:id>',views.cleer,name='cleer'),
    path('add_unit',views.add_unit,name='add_unit'),
    path('sales',views.add_sales,name='add_sales'),
    path('sample/',views.sample,name="sample"),
    path('view_vendor_list/',views.view_vendor_list,name='view_vendor_list'),
    path('view_vendor_details/<int:pk>',views.view_vendor_details,name='view_vendor_details'),
    path('add_comment/<int:pk>',views.add_comment,name='add_comment'),
    path('sendmail/<int:pk>',views.sendmail,name='sendmail'),
    path('edit_vendor/<int:pk>',views.edit_vendor,name='edit_vendor'),
    path('edit_vendor_details/<int:pk>',views.edit_vendor_details,name='edit_vendor_details'),
    path('upload_document/<int:pk>',views.upload_document,name='upload_document'),
    path('download_doc/<int:pk>',views.download_doc,name='download_doc'),
    path('cancel_vendor/',views.cancel_vendor,name='cancel_vendor'),
    path('delete_vendor/<int:pk>',views.delete_vendor,name='delete_vendor'),
    path('add_customer/',views.add_customer,name='add_customer'),
    path('retainer_invoices/',views.retainer_invoice,name='retainer_invoice'),
    path('add_invoice/',views.add_invoice,name='add_invoice'),
    path('create_invoice_draft/',views.create_invoice_draft,name='create_invoice_draft'),
    path('create_invoice_send/',views.create_invoice_send,name='create_invoice_send'),
    path('view_invoice/<int:pk>',views.invoice_view,name='invoice_view'),
    path('retainer_template/<int:pk>',views.retainer_template,name='retainer_template'),
    path('retainer_invoice_edit/<int:pk>',views.retainer_edit_page,name='retainer_edit_page'), 
    path('retainer_invoice_update/<int:pk>',views.retainer_update,name='retainer_update'),
    path('send_mail/<int:pk>',views.mail_send,name='mail_send'),
    path('retaineritem_delete/<int:pk>',views.retaineritem_delete,name='retaineritem_delete'),
    path('retainer_delete/<int:pk>',views.retainer_delete,name='retainer_delete'),
    path('allestimates',views.allestimates,name='allestimates'),
    path('newestimate/',views.newestimate,name='newestimate'),
    path('createestimate/',views.createestimate,name='createestimate'),
    path('itemdata_est/',views.itemdata_est,name='itemdata_est'),
    path('create_and_send_estimate/',views.create_and_send_estimate,name='create_and_send_estimate'),
    path('estimateslip/<int:est_id>',views.estimateslip,name='estimateslip'),
    path('editestimate/<int:est_id>',views.editestimate,name='editestimate'),
    path('updateestimate/<int:pk>',views.updateestimate,name='updateestimate'),
    path('converttoinvoice/<int:est_id>',views.converttoinvoice,name='converttoinvoice'),
    path('emailattachment', EmailAttachementView.as_view(), name='emailattachment'),
    path('add_customer_for_estimate/',views.add_customer_for_estimate,name='add_customer_for_estimate'),
    path('entr_custmr_for_estimate/',views.entr_custmr_for_estimate,name='entr_custmr_for_estimate'),
    path('payment_term_for_estimate/',views.payment_term_for_estimate,name='payment_term_for_estimate'),
    path('invoiceview',views.invoiceview,name='invoiceview'),
    path('addinvoice',views.addinvoice,name='addinvoice'),
    path('itemdata',views.itemdata,name='itemdata'),
    path('add_prod',views.add_prod,name='add_prod'),
    path('detailedview/<int:id>',views.detailedview,name='detailedview'),
    path('edited_prod/<int:id>',views.edited_prod,name='edited_prod'),
    path('dele/<int:pk>',views.dele,name='dele'),
    # path('edited/<int:id>',views.edited,name='edited'),
    path('payment_term',views.payment_term,name='payment_term'),
    path('add_cx',views.add_cx,name="add_cx"),
    path('deleteestimate/<int:est_id>',views.deleteestimate,name='deleteestimate'),
    path('additem_est',views.additem_est,name='additem_est'),
    path('additem_page_est',views.additem_page_est,name='additem_page_est'),
    path('add_unit_est',views.add_unit_est,name='add_unit_est'),
    path('add_sales_est',views.add_sales_est,name='add_sales_est'),
    path('add_account_est',views.add_account_est,name='add_account_est'),
    path('customerdata', views.customerdata, name='customerdata'),
    path('add_customer_for_invoice',views.add_customer_for_invoice,name='add_customer_for_invoice'),
    path('payment_term_for_invoice',views.payment_term_for_invoice,name='payment_term_for_invoice'),
    path('addprice',views.addprice,name='addprice'),
    path('addpl',views.addpl,name='addpl'),
    path('viewpricelist',views.viewpricelist,name='viewpricelist'),
    path('viewlist/<int:id>',views.viewlist,name='viewlist'),
    path('editlist/<int:id>',views.editlist,name='editlist'),
    path('editpage/<int:id>',views.editpage,name='editpage'),
    path('delete_item/<int:id>',views.delete_item,name='delete_item'),
    path('active_status/<int:id>',views.active_status,name='active_status'),
    path('createpl',views.createpl,name='createpl'),
    path('banking_home',views.banking_home,name='banking_home'),
    path('create_banking',views.create_banking,name='create_banking'),
    path('save_banking',views.save_banking,name='save_banking'),
    path('view_bank/<int:id>',views.view_bank,name='view_bank'),
    path('banking_edit/<int:id>',views.banking_edit,name='banking_edit'),
    path('save_edit_bnk/<int:id>',views.save_edit_bnk,name='save_edit_bnk'),
    path('save_banking_edit/<int:id>',views.save_banking_edit,name='save_banking_edit'),
    path('save_bank',views.save_bank,name='save_bank'),
    path('entr_custmr',views.entr_custmr,name='entr_custmr'),
    path('payment_term',views.payment_term,name='payment_term'),
    path('get_customer_names', views.get_customer_names, name='get_customer_names'),
    path('expense/delete/<int:expense_id>/', views.delete_expense, name='delete_expense'),
    path('get_profile_details/<int:profile_id>/', views.get_profile_details, name='get_profile_details'),
    path('recurringhome',views.recurringhome,name='recurringhome'),
    path('add_expense',views.add_expense,name='add_expense'),
    path('recurringbase',views.recurringbase,name='recurringbase'),
    path('show_recurring/<int:expense_id>/', views.show_recurring, name='show_recurring'),
    path('expense_details', views.expense_details, name='expense_details'),
    path('vendor/',views.vendor,name='vendor'),
    path('add_vendor/',views.add_vendor,name='add_vendor'),
    path('edit_expense/<int:expense_id>/', views.edit_expense, name='edit_expense'),
    path('newexp',views.newexp,name='newexp'),
    path('save-data/', save_data, name='save_data'),
    path('get-account-names/', views.get_account_names, name='get_account_names'),
    path('profileshow',views.profileshow,name='profileshow'),
    path('add_customer',views.add_customer,name='add_customer'),
    path('entr_custmr',views.entr_custmr,name='entr_custmr'),
    path('payment_term',views.payment_term,name='payment_term'),



    
    path('view_sales_order',views.view_sales_order,name='view_sales_order'),
    path('create_sales_order',views.create_sales_order,name='create_sales_order'),
    path('add_customer_for_sorder',views.add_customer_for_sorder,name='add_customer_for_sorder'),
    path('payment_term_for_sorder',views.payment_term_for_sorder,name='payment_term_for_sorder'),

    path('add_sales_order',views.add_sales_order,name='add_sales_order'),
    path('sales_order_det/<int:id>',views.sales_order_det,name='sales_order_det'),
    path('edit_sales_order/<int:id>',views.edit_sales_order,name='edit_sales_order'),
    path('delet_sales/<int:id>',views.delet_sales,name='delet_sales'),

    
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),

#------------------------------------------------------------------------------------------------sumayya---purchase bills
    path('view_bills',views.view_bills,name='view_bills'),
    path('new_bill/',views.new_bill,name='new_bill'),
    path('get_customer_data_bill/',views.get_customer_data_bill,name='get_customer_data_bill'),
    path('get_vendor_data_bill/',views.get_vendor_data_bill,name='get_vendor_data_bill'),
    path('create_purchase_bill/',views.create_purchase_bill,name='create_purchase_bill'),
    path('create_purchase_bill1/',views.create_purchase_bill1,name='create_purchase_bill1'),
    path('itemdata_bills/',views.itemdata_bills,name='itemdata_bills'),
    path('bill_view/<int:b_id>',views.bill_view,name='bill_view'),
    path('edit_bill/<int:bill_id>',views.edit_bill,name='edit_bill'),
    path('update_bills/<int:pk>',views.update_bills,name='update_bills'),
    path('add_comment_bills/<int:bill_id>',views.add_comment_bills,name='add_comment_bills'),
    path('upload_file_bills/<int:bill_id>',views.upload_file_bills,name='upload_file_bills'),
    path('delete_bill/<int:bill_id>',views.delete_bill,name='delete_bill'),
    path('search_bill/',views.search_bill,name='search_bill'),
    
    path('entr_custmr_for_bills/',views.entr_custmr_for_bills,name='entr_custmr_for_bills'),
    path('add_vendor_bills/',views.add_vendor_bills,name='add_vendor_bills'),
    path('additem_bills/',views.additem_bills,name='additem_bills'),
    path('create_account_bills/',views.create_account_bills,name='create_account_bills'),
    path('create_payment_terms_bills/',views.create_payment_terms_bills,name='create_payment_terms_bills'),

    path('add_sales_bills/',views.add_sales_bills,name='add_sales_bills'),
    # path('add_unit_bills/',views.add_unit_bills,name='add_unit_bills'),

    # path('payment_term_for_bills/',views.payment_term_for_bills,name='payment_term_for_bills'),
    # path('payment_term_for_bills1/',views.payment_term_for_bills1,name='payment_term_for_bills1'),
    # path('converttoinvoice/<int:est_id>',views.converttoinvoice,name='converttoinvoice'),
    # path('emailattachment', EmailAttachementView.as_view(), name='emailattachment'),
    # path('add_customer_for_bills/',views.add_customer_for_bills,name='add_customer_for_bills'),
    # path('add_account_bills/',views.add_account_bills,name='add_account_bills'),

    
    
    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
