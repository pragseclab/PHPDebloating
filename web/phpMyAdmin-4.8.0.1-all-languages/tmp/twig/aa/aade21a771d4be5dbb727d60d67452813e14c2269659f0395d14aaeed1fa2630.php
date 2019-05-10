<?php

/* privileges/add_user_fieldset.twig */
class __TwigTemplate_b1b6a4782f91dd7a82b56bf19c35e6ebd904c9c4933bf15fc64cc98ba56fa9c3 extends Twig_Template
{
    public function __construct(Twig_Environment $env)
    {
        parent::__construct($env);

        $this->parent = false;

        $this->blocks = array(
        );
    }

    protected function doDisplay(array $context, array $blocks = array())
    {
        // line 1
        echo "<fieldset id=\"fieldset_add_user\">
    <legend>";
        // line 2
        echo _pgettext(        "Create new user", "New");
        echo "</legend>
    <a id=\"add_user_anchor\" href=\"server_privileges.php";
        // line 3
        echo PhpMyAdmin\Url::getCommon((isset($context["url_params"]) ? $context["url_params"] : null));
        echo "\"
        ";
        // line 4
        if ( !twig_test_empty((isset($context["rel_params"]) ? $context["rel_params"] : null))) {
            // line 5
            echo "            rel=\"";
            echo PhpMyAdmin\Url::getCommon((isset($context["rel_params"]) ? $context["rel_params"] : null));
            echo "\"
        ";
        }
        // line 6
        echo ">
        ";
        // line 7
        echo PhpMyAdmin\Util::getIcon("b_usradd");
        echo _gettext("Add user account");
        echo "</a>
</fieldset>
";
    }

    public function getTemplateName()
    {
        return "privileges/add_user_fieldset.twig";
    }

    public function isTraitable()
    {
        return false;
    }

    public function getDebugInfo()
    {
        return array (  41 => 7,  38 => 6,  32 => 5,  30 => 4,  26 => 3,  22 => 2,  19 => 1,);
    }

    /** @deprecated since 1.27 (to be removed in 2.0). Use getSourceContext() instead */
    public function getSource()
    {
        @trigger_error('The '.__METHOD__.' method is deprecated since version 1.27 and will be removed in 2.0. Use getSourceContext() instead.', E_USER_DEPRECATED);

        return $this->getSourceContext()->getCode();
    }

    public function getSourceContext()
    {
        return new Twig_Source("", "privileges/add_user_fieldset.twig", "/var/www/html/phpMyAdmin-4.8.0.1-all-languages/templates/privileges/add_user_fieldset.twig");
    }
}
