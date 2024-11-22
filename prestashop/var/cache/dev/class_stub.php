<?php

class Link extends LinkCore {};
class Group extends GroupCore {};
class WarehouseProductLocation extends WarehouseProductLocationCore {};
class StockMvt extends StockMvtCore {};
class SupplyOrderState extends SupplyOrderStateCore {};
class SupplyOrderHistory extends SupplyOrderHistoryCore {};
class StockAvailable extends StockAvailableCore {};
class Warehouse extends WarehouseCore {};
class Stock extends StockCore {};
class StockManager extends StockManagerCore {};
class StockManagerFactory extends StockManagerFactoryCore {};
class SupplyOrderDetail extends SupplyOrderDetailCore {};
class StockMvtWS extends StockMvtWSCore {};
class SupplyOrderReceiptHistory extends SupplyOrderReceiptHistoryCore {};
class StockMvtReason extends StockMvtReasonCore {};
class SupplyOrder extends SupplyOrderCore {};
abstract class StockManagerModule extends StockManagerModuleCore {};
class CustomizationField extends CustomizationFieldCore {};
class Contact extends ContactCore {};
class ConfigurationTest extends ConfigurationTestCore {};
class ProductAssembler extends ProductAssemblerCore {};
class GroupReduction extends GroupReductionCore {};
class WebserviceOutputJSON extends WebserviceOutputJSONCore {};
class WebserviceKey extends WebserviceKeyCore {};
class WebserviceSpecificManagementAttachments extends WebserviceSpecificManagementAttachmentsCore {};
class WebserviceException extends WebserviceExceptionCore {};
class WebserviceOutputBuilder extends WebserviceOutputBuilderCore {};
class WebserviceOutputXML extends WebserviceOutputXMLCore {};
class WebserviceSpecificManagementImages extends WebserviceSpecificManagementImagesCore {};
class WebserviceSpecificManagementSearch extends WebserviceSpecificManagementSearchCore {};
class WebserviceRequest extends WebserviceRequestCore {};
class TemplateFinder extends TemplateFinderCore {};
class SmartyResourceModule extends SmartyResourceModuleCore {};
class SmartyCustomTemplate extends SmartyCustomTemplateCore {};
class SmartyResourceParent extends SmartyResourceParentCore {};
class SmartyCustom extends SmartyCustomCore {};
class SmartyDevTemplate extends SmartyDevTemplateCore {};
class PhpEncryptionEngine extends PhpEncryptionEngineCore {};
class CustomerAddressFormatter extends CustomerAddressFormatterCore {};
class CustomerAddressPersister extends CustomerAddressPersisterCore {};
class CustomerLoginFormatter extends CustomerLoginFormatterCore {};
class CustomerLoginForm extends CustomerLoginFormCore {};
class CustomerForm extends CustomerFormCore {};
class FormField extends FormFieldCore {};
abstract class AbstractForm extends AbstractFormCore {};
class CustomerPersister extends CustomerPersisterCore {};
class CustomerAddressForm extends CustomerAddressFormCore {};
class CustomerFormatter extends CustomerFormatterCore {};
class Tag extends TagCore {};
class Product extends ProductCore {};
class DbMySQLi extends DbMySQLiCore {};
class DbPDO extends DbPDOCore {};
abstract class Db extends DbCore {};
class DbQuery extends DbQueryCore {};
class PhpEncryption extends PhpEncryptionCore {};
class Risk extends RiskCore {};
class Context extends ContextCore {};
class Profile extends ProfileCore {};
class CSV extends CSVCore {};
class Search extends SearchCore {};
class Delivery extends DeliveryCore {};
class QuickAccess extends QuickAccessCore {};
class Attachment extends AttachmentCore {};
class HTMLTemplateOrderSlip extends HTMLTemplateOrderSlipCore {};
class PDF extends PDFCore {};
class HTMLTemplateSupplyOrderForm extends HTMLTemplateSupplyOrderFormCore {};
abstract class HTMLTemplate extends HTMLTemplateCore {};
class HTMLTemplateDeliverySlip extends HTMLTemplateDeliverySlipCore {};
class HTMLTemplateInvoice extends HTMLTemplateInvoiceCore {};
class PDFGenerator extends PDFGeneratorCore {};
class HTMLTemplateOrderReturn extends HTMLTemplateOrderReturnCore {};
class ImageType extends ImageTypeCore {};
abstract class PaymentModule extends PaymentModuleCore {};
class ConnectionsSource extends ConnectionsSourceCore {};
class Category extends CategoryCore {};
class OrderStateLang extends OrderStateLangCore {};
class CarrierLang extends CarrierLangCore {};
class DataLang extends DataLangCore {};
class RiskLang extends RiskLangCore {};
class QuickAccessLang extends QuickAccessLangCore {};
class ThemeLang extends ThemeLangCore {};
class SupplyOrderStateLang extends SupplyOrderStateLangCore {};
class CmsCategoryLang extends CmsCategoryLangCore {};
class AttributeLang extends AttributeLangCore {};
class FeatureLang extends FeatureLangCore {};
class FeatureValueLang extends FeatureValueLangCore {};
class GenderLang extends GenderLangCore {};
class TabLang extends TabLangCore {};
class AttributeGroupLang extends AttributeGroupLangCore {};
class OrderMessageLang extends OrderMessageLangCore {};
class MetaLang extends MetaLangCore {};
class StockMvtReasonLang extends StockMvtReasonLangCore {};
class CategoryLang extends CategoryLangCore {};
class ContactLang extends ContactLangCore {};
class ConfigurationLang extends ConfigurationLangCore {};
class ProfileLang extends ProfileLangCore {};
class GroupLang extends GroupLangCore {};
class OrderReturnStateLang extends OrderReturnStateLangCore {};
class Referrer extends ReferrerCore {};
abstract class AbstractCheckoutStep extends AbstractCheckoutStepCore {};
class DeliveryOptionsFinder extends DeliveryOptionsFinderCore {};
class CartChecksum extends CartChecksumCore {};
class PaymentOptionsFinder extends PaymentOptionsFinderCore {};
class CheckoutSession extends CheckoutSessionCore {};
class AddressValidator extends AddressValidatorCore {};
class CheckoutDeliveryStep extends CheckoutDeliveryStepCore {};
class CheckoutPaymentStep extends CheckoutPaymentStepCore {};
class ConditionsToApproveFinder extends ConditionsToApproveFinderCore {};
class CheckoutPersonalInformationStep extends CheckoutPersonalInformationStepCore {};
class CheckoutAddressesStep extends CheckoutAddressesStepCore {};
class CheckoutProcess extends CheckoutProcessCore {};
class Uploader extends UploaderCore {};
class ManufacturerAddress extends ManufacturerAddressCore {};
class AddressChecksum extends AddressChecksumCore {};
class Curve extends CurveCore {};
class ProductSale extends ProductSaleCore {};
class RequestSql extends RequestSqlCore {};
class Alias extends AliasCore {};
class EmployeeSession extends EmployeeSessionCore {};
class Access extends AccessCore {};
class OrderHistory extends OrderHistoryCore {};
class OrderReturnState extends OrderReturnStateCore {};
class OrderReturn extends OrderReturnCore {};
class OrderDetail extends OrderDetailCore {};
class OrderPayment extends OrderPaymentCore {};
class OrderMessage extends OrderMessageCore {};
class OrderInvoice extends OrderInvoiceCore {};
class OrderDiscount extends OrderDiscountCore {};
class OrderState extends OrderStateCore {};
class OrderCartRule extends OrderCartRuleCore {};
class OrderCarrier extends OrderCarrierCore {};
class Order extends OrderCore {};
class OrderSlip extends OrderSlipCore {};
class AddressFormat extends AddressFormatCore {};
class Dispatcher extends DispatcherCore {};
class Media extends MediaCore {};
class AttributeGroup extends AttributeGroupCore {};
class FeatureValue extends FeatureValueCore {};
class Tab extends TabCore {};
class Hook extends HookCore {};
class CustomerSession extends CustomerSessionCore {};
class CacheXcache extends CacheXcacheCore {};
class CacheApc extends CacheApcCore {};
class CacheMemcache extends CacheMemcacheCore {};
class CacheMemcached extends CacheMemcachedCore {};
abstract class Cache extends CacheCore {};
class Validate extends ValidateCore {};
class Tools extends ToolsCore {};
class SearchEngine extends SearchEngineCore {};
class Supplier extends SupplierCore {};
class PhpEncryptionLegacyEngine extends PhpEncryptionLegacyEngineCore {};
class Message extends MessageCore {};
class SpecificPriceRule extends SpecificPriceRuleCore {};
class RangePrice extends RangePriceCore {};
class RangeWeight extends RangeWeightCore {};
class Cart extends CartCore {};
class Currency extends CurrencyCore {};
class CMSRole extends CMSRoleCore {};
class Cookie extends CookieCore {};
class Translate extends TranslateCore {};
class Guest extends GuestCore {};
class Page extends PageCore {};
abstract class TreeToolbarButton extends TreeToolbarButtonCore {};
class Tree extends TreeCore {};
class TreeToolbarSearch extends TreeToolbarSearchCore {};
class TreeToolbarLink extends TreeToolbarLinkCore {};
class TreeToolbar extends TreeToolbarCore {};
class TreeToolbarSearchCategories extends TreeToolbarSearchCategoriesCore {};
class Upgrader extends UpgraderCore {};
class State extends StateCore {};
abstract class ModuleGridEngine extends ModuleGridEngineCore {};
abstract class Module extends ModuleCore {};
abstract class ModuleGraph extends ModuleGraphCore {};
abstract class ModuleGraphEngine extends ModuleGraphEngineCore {};
abstract class CarrierModule extends CarrierModuleCore {};
abstract class ModuleGrid extends ModuleGridCore {};
class Shop extends ShopCore {};
class ShopUrl extends ShopUrlCore {};
class ShopGroup extends ShopGroupCore {};
class CustomerMessage extends CustomerMessageCore {};
class ProductSupplier extends ProductSupplierCore {};
class Carrier extends CarrierCore {};
class Image extends ImageCore {};
class Country extends CountryCore {};
class LocalizationPack extends LocalizationPackCore {};
class Tax extends TaxCore {};
class TaxRulesTaxManager extends TaxRulesTaxManagerCore {};
class TaxRulesGroup extends TaxRulesGroupCore {};
class TaxManagerFactory extends TaxManagerFactoryCore {};
abstract class TaxManagerModule extends TaxManagerModuleCore {};
class TaxCalculator extends TaxCalculatorCore {};
class TaxConfiguration extends TaxConfigurationCore {};
class TaxRule extends TaxRuleCore {};
class FileUploader extends FileUploaderCore {};
class Configuration extends ConfigurationCore {};
class Notification extends NotificationCore {};
class DateRange extends DateRangeCore {};
class Zone extends ZoneCore {};
class CustomerThread extends CustomerThreadCore {};
class Windows extends WindowsCore {};
class Employee extends EmployeeCore {};
class FileLogger extends FileLoggerCore {};
abstract class AbstractLogger extends AbstractLoggerCore {};
class Meta extends MetaCore {};
abstract class ObjectModel extends ObjectModelCore {};
class Connection extends ConnectionCore {};
class SpecificPrice extends SpecificPriceCore {};
class WarehouseAddress extends WarehouseAddressCore {};
class CMSCategory extends CMSCategoryCore {};
abstract class AbstractAssetManager extends AbstractAssetManagerCore {};
class JavascriptManager extends JavascriptManagerCore {};
class CssMinifier extends CssMinifierCore {};
class StylesheetManager extends StylesheetManagerCore {};
class CccReducer extends CccReducerCore {};
class JsMinifier extends JsMinifierCore {};
class ValidateConstraintTranslator extends ValidateConstraintTranslatorCore {};
class Attribute extends AttributeCore {};
class PrestaShopBackup extends PrestaShopBackupCore {};
class SpecificPriceFormatter extends SpecificPriceFormatterCore {};
class PrestaShopCollection extends PrestaShopCollectionCore {};
class Address extends AddressCore {};
class AdminController extends AdminControllerCore {};
abstract class ProductListingFrontController extends ProductListingFrontControllerCore {};
abstract class Controller extends ControllerCore {};
class ModuleFrontController extends ModuleFrontControllerCore {};
abstract class ModuleAdminController extends ModuleAdminControllerCore {};
abstract class ProductPresentingFrontController extends ProductPresentingFrontControllerCore {};
class FrontController extends FrontControllerCore {};
class QqUploadedFileXhr extends QqUploadedFileXhrCore {};
class Feature extends FeatureCore {};
class ConfigurationKPI extends ConfigurationKPICore {};
class CustomerAddress extends CustomerAddressCore {};
class Customer extends CustomerCore {};
class ProductDownload extends ProductDownloadCore {};
class HelperShop extends HelperShopCore {};
class HelperTreeShops extends HelperTreeShopsCore {};
class HelperKpiRow extends HelperKpiRowCore {};
class HelperView extends HelperViewCore {};
class HelperCalendar extends HelperCalendarCore {};
class HelperOptions extends HelperOptionsCore {};
class HelperKpi extends HelperKpiCore {};
class HelperImageUploader extends HelperImageUploaderCore {};
class HelperList extends HelperListCore {};
class HelperUploader extends HelperUploaderCore {};
class HelperTreeCategories extends HelperTreeCategoriesCore {};
class Helper extends HelperCore {};
class HelperForm extends HelperFormCore {};
class QqUploadedFileForm extends QqUploadedFileFormCore {};
class TranslatedConfiguration extends TranslatedConfigurationCore {};
class CMS extends CMSCore {};
class Pack extends PackCore {};
class PrestaShopModuleException extends PrestaShopModuleExceptionCore {};
class PrestaShopDatabaseException extends PrestaShopDatabaseExceptionCore {};
class PrestaShopException extends PrestaShopExceptionCore {};
class PrestaShopObjectNotFoundException extends PrestaShopObjectNotFoundExceptionCore {};
class PrestaShopPaymentException extends PrestaShopPaymentExceptionCore {};
class Store extends StoreCore {};
class Combination extends CombinationCore {};
class Customization extends CustomizationCore {};
class CartRule extends CartRuleCore {};
class ProductPresenterFactory extends ProductPresenterFactoryCore {};
class Gender extends GenderCore {};
class SupplierAddress extends SupplierAddressCore {};
class Chart extends ChartCore {};
class ImageManager extends ImageManagerCore {};
class Mail extends MailCore {};
class PrestaShopLogger extends PrestaShopLoggerCore {};
class Language extends LanguageCore {};
class Manufacturer extends ManufacturerCore {};
class LinkProxy extends LinkProxyCore {};